import importlib
import json
import logging
import os
import re
import sys


log = logging.getLogger(__name__)


class Pijon():

    def __init__(self, migration_folder, files_format='migration_\d+_.*'):
        sys.path.append(migration_folder)
        self.folder = migration_folder
        self.files_format = files_format
        self.migrations = self.list_migrations()

    @classmethod
    def list(cls, migrations_folder='./pijon', file_format='migration_\d+_.*'):
        return Pijon(migrations_folder).migrations

    def list_migrations(self):
        files = os.listdir(self.folder)
        regex = re.compile("({})\.py$".format(self.files_format))
        migrations = [
            regex.findall(file)[0]
            for file in files
            if regex.findall(file)
        ]
        log.debug("Migrations steps found {}".format(migrations))
        return migrations

    def migrate_step(self, step, data):
        """
        Perform a migration step
        """
        log.debug("Migrating step {}".format(step))
        folder = re.findall('[^\/]+$', self.folder)[0]
        module = "{folder}.{step}".format(folder=folder, step=step)
        importlib.import_module(module)
        return sys.modules[module].migrate(data)

    def _migrate(self, input_data):
        """
        perform all migrations registered
        """
        data = input_data
        for step in self.migrations:
            data = self.migrate_step(step, data)
        return data

    @classmethod
    def migrate(cls, in_data, direct_input=False, direct_output=False, output_filename=None,
                migrations_folder='./pijon', file_format='migration_\d+_.*'):
        """
        migrate a given json file.
        if output_filename is not given, update the input file
        if out is True returns the content rather than writting to file
        """
        pijon = Pijon(migrations_folder, file_format)
        input_json = None
        if direct_input:
            input_data = json.loads(in_data)
        else:
            with open(in_data, 'r') as input_file:
                input_data = json.loads(input_file.read())

        result = pijon._migrate(input_data)
        if direct_output:
            return json.dumps(result)
        else:
            if output_filename is None:
                output_filename = input_filename
                log.info('No output file name provided, the input one will be updated')

            with open(output_filename, 'w') as output_file:
                json.dump(
                    result, output_file,
                    sort_keys=True, indent=4, separators=(',', ': ')
                )
