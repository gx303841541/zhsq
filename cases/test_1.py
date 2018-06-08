# -*- coding: utf-8 -*-
import datetime
import json
import os
import random
import re
import sys
import time
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abs_path)

import case_tools.case_actions as case_actions
from APIs.common_APIs import modify_cls, modify_init
from case_config import config
import case_config.test_1 as test_1

@modify_init(casename="Test_getFileList", log_dir="D:\\it\\result\\20180607_151549-test_1\\")
class Test_getFileList(case_actions.Action):
    def setup(self):
        self.do_setup(test_1.Test_getFileList)
    def run(self):
        self.do_run(test_1.Test_getFileList)
    def teardown(self):
        self.do_teardown(test_1.Test_getFileList)


