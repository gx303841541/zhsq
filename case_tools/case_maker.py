#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""ATS framework
by Kobe Gong 2017-8-21
use:
    define testcase interface follow nose's case
"""

import datetime
import os
import re
import shutil
import sys
import traceback
from abc import ABCMeta, abstractmethod
from importlib import import_module

import APIs.common_APIs as common_APIs
import case_config.config as config


def clear_case_files():
    for file in os.listdir('./cases'):
        if '__' not in file:
            try:
                os.remove('./cases/%s' % file)
            except Exception as e:
                shutil.rmtree('./cases/%s' % file)


class CaseMaker(object):
    def __init__(self, logger, config_file):
        self.LOG = logger
        self.config_file = config_file
        self.create_dir()
        self.make()

    def create_dir(self):
        try:
            log_dir = config.work_dir + os.path.sep + 'result' + \
                os.path.sep + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + \
                '-' + self.config_file + os.path.sep
            os.mkdir(log_dir)
            self.log_dir = log_dir
        except Exception as er:
            self.LOG.error('Can not create log dir: %s\n[[%s]]' % (
                log_dir, str(er)))
            sys.exit()

    def make(self):
        self.LOG.info("To create cases for: %s" % self.config_file)
        config_file = config.work_dir + os.path.sep + \
            'case_config' + os.path.sep + self.config_file + '.py'
        case_file = config.work_dir + os.path.sep + \
            'cases' + os.path.sep + self.config_file + '.py'
        config_module = import_module('case_config.' + self.config_file)
        with open(case_file, 'w') as cf:
            self.build_head(cf)
            for casename in config_module.cases:
                self.build_class(cf, casename=casename)

            self.build_end(cf)
        return case_file

    def build_head(self, cf):
        cf.write('# -*- coding: utf-8 -*-\n')
        cf.write('import datetime\n')
        cf.write('import json\n')
        cf.write('import os\n')
        cf.write('import random\n')
        cf.write('import re\n')
        cf.write('import sys\n')
        cf.write('import time\n')
        cf.write('abs_path = os.path.abspath(os.path.dirname(__file__))\n')
        cf.write('sys.path.append(os.path.dirname(abs_path))\n')
        cf.write('\n')
        cf.write('import case_tools.case_actions as case_actions\n')
        cf.write('from APIs.common_APIs import modify_cls, modify_init\n')
        cf.write('from case_config import config\n')
        cf.write('import case_config.%s as %s\n' %
                 (self.config_file, self.config_file))
        cf.write('\n')

    def build_class(self, cf, casename):
        cf.write('@modify_init(casename="%s", log_dir="%s")\n' %
                 (casename, common_APIs.dirit(self.log_dir)))
        cf.write('class %s(case_actions.Action):\n' % (casename))
        self.build_setup(cf, casename)
        self.build_step(cf, casename)
        self.build_teardown(cf, casename)
        cf.write('\n\n')

    def build_setup(self, cf, casename):
        cf.write('    def setup(self):\n')
        cf.write('        self.do_setup(%s.cases["%s"])\n' %
                 (self.config_file, casename))

    def build_step(self, cf, casename):
        cf.write('    def run(self):\n')
        cf.write('        self.do_run(%s.cases["%s"])\n' %
                 (self.config_file, casename))

    def build_teardown(self, cf, casename):
        cf.write('    def teardown(self):\n')
        cf.write('        self.do_teardown(%s.cases["%s"])\n' %
                 (self.config_file, casename))

    def build_end(self, cf):
        pass
