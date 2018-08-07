# -*- coding: utf-8 -*-
import datetime
import json
import os
import random
import re
import sys
import time
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.dirname(abs_path))

import case_tools.case_actions as case_actions
from APIs.common_APIs import modify_cls, modify_init
from case_config import config
import case_config.pay_test as pay_test

@modify_init(casename="Test_pay1", log_dir="C:\\zhsq\\result\\20180806_180815-pay_test\\")
class Test_pay1(case_actions.Action):
    def setup(self):
        self.do_setup(pay_test.cases["Test_pay1"])
    def run(self):
        self.do_run(pay_test.cases["Test_pay1"])
    def teardown(self):
        self.do_teardown(pay_test.cases["Test_pay1"])


@modify_init(casename="Test_pay2", log_dir="C:\\zhsq\\result\\20180806_180815-pay_test\\")
class Test_pay2(case_actions.Action):
    def setup(self):
        self.do_setup(pay_test.cases["Test_pay2"])
    def run(self):
        self.do_run(pay_test.cases["Test_pay2"])
    def teardown(self):
        self.do_teardown(pay_test.cases["Test_pay2"])


