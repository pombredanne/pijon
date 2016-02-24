#!/usr/bin/env python

import collections
from importlib import machinery
import logging
import os
import re
import sys


__all__ = ['Pijon', 'migrate']


log = logging.getLogger(__name__)


def migrate(data, in_place=True, folder=None):
    p = Pijon(folder)
    return p.migrate(data, in_place=in_place)


class Pijon(object):

    DEFAULT_FOLDER = 'migrations'
    MIGRATION_REGEX = r'(?P<ident>\d{4})_(?P<name>\w+)\.py'

    def __init__(self, folder=None):
        self.folder = folder or self.DEFAULT_FOLDER
        self.migrations = self.retrieve_migrations()

    @property
    def last_migration(self):
        """
        Returns last migration identity number
        """
        return int(next(reversed(self.migrations)))

    def retrieve_migrations(self):
        migrations = collections.OrderedDict()
        for filename in sorted(os.listdir(self.folder)):
            match = re.match(self.MIGRATION_REGEX, filename)
            if not match:
                log.debug('pass: %s', filename)
                continue

            # Match migration filename pattern
            ident = match.group('ident')
            name = match.group('name')

            # Load module
            module = machinery.SourceFileLoader(
                name, os.path.join(self.folder, filename)
            ).load_module(name)

            migrations[ident] = module
            log.info("Loaded module '%s'", module)

        return migrations

    def migrate(self, data, in_place=True):
        new = data.copy() if not in_place else None
        for ident, module in self.migrations.items():
            module.migrate(new if new else data)
        return new if new else data


if __name__ == '__main__':
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)5s %(asctime)s [%(name)s] %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

    data = {'one': 'hello', 'two': 'yo'}
    print(data)
    new = migrate(data, in_place=False)
    print(new)
    print(data)
