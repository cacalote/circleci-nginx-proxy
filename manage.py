#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

import os
import sys

from flask.ext.script import Manager, Server
from flask.ext.script.commands import Command, ShowUrls, Clean

from foob import create_app


def test(marker="not web and not integration"):
    test_args = ['--strict', '--verbose', '--tb=long', 'tests', '-m', marker]
    import pytest
    errno = pytest.main(test_args)
    sys.exit(errno)

class Test(Command):
    def run(self):
        self.test_suite = True
        test()

env = os.environ.get('FOOB_ENV', 'dev')
app = create_app('foob.settings.%sConfig' % env.capitalize())

manager = Manager(app)
manager.add_command("server", Server)
manager.add_command("show-urls", ShowUrls)
manager.add_command("clean", Clean)
manager.add_command("test", Test)

if __name__ == "__main__":
    manager.run()
