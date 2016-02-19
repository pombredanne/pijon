import importlib
import json
import logging
import os
import re
import sys


log = logging.getLogger(__name__)


class Pijon():

    def __init__(self, folder, data, files_format='.+'):
        sys.path.append(folder)
        self.folder = folder
        self.files_format = files_format
        self.migrations = self.list_migrations()
        self.data = data

    def list_migrations(self):
        files = os.listdir(self.folder)
        regex = re.compile("({})\.py".format(self.files_format))
        migrations = [
            regex.findall(file)[0]
            for file in files
            if regex.findall(file)
        ]
        log.debug("Migrations steps found {}".format(migrations))
        return migrations

    @classmethod
    def _migrate(cls, input_data, migrations_folder, file_format='.+'):
        """
        perform all migrations registered
        """
        pijon = Pijon(migrations_folder, input_data, file_format)
        for step in pijon.migrations:
            pijon.migrate_step(step)
        return pijon.data

    @classmethod
    def migrate(cls, input_json, migrations_folder, file_format='.+'):
        """
        migrate a given json input
        """
        data = json.loads(input_json)
        result = cls._migrate(data, migrations_folder, file_format)
        return json.dumps(result)

    @classmethod
    def migrate_file(cls, input_filename, migrations_folder,
                     output_filename=None, file_format='.+'):
        """
        migrate a given json file.
        if output_file is not given, update the input file
        """
        with open(input_filename, 'r') as input_file:
            result = cls._migrate(
                json.loads(input_file.read()),
                migrations_folder,
                file_format
            )

        if output_filename is None:
            output_filename = input_filename
            log.info('No output file name provided, the input one will be updated')

        with open(output_filename, 'w') as output_file:
            json.dump(
                result, output_file,
                sort_keys=True, indent=4, separators=(',', ': ')
            )

    def migrate_step(self, step):
        """
        Perform a migration step
        """
        log.debug("Migrating step {}".format(step))
        folder = re.findall('[^\/]+$', self.folder)[0]
        module = "{folder}.{step}".format(folder=folder, step=step)
        importlib.import_module(module)
        sys.modules[module].migrate(self.data)
