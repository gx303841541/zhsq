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
import case_config.dial_test as dial_test

@modify_init(casename="Test_faceswipEvent", log_dir="C:\\zhsq\\result\\20180712_101253-dial_test\\")
class Test_faceswipEvent(case_actions.Action):
    def setup(self):
        self.do_setup(dial_test.cases["Test_faceswipEvent"])
    def run(self):
        self.do_run(dial_test.cases["Test_faceswipEvent"])
    def teardown(self):
        self.do_teardown(dial_test.cases["Test_faceswipEvent"])


@modify_init(casename="Test_patrolHandle", log_dir="C:\\zhsq\\result\\20180712_101253-dial_test\\")
class Test_patrolHandle(case_actions.Action):
    def setup(self):
        self.do_setup(dial_test.cases["Test_patrolHandle"])
    def run(self):
        self.do_run(dial_test.cases["Test_patrolHandle"])
    def teardown(self):
        self.do_teardown(dial_test.cases["Test_patrolHandle"])


@modify_init(casename="Test_playshow", log_dir="C:\\zhsq\\result\\20180712_101253-dial_test\\")
class Test_playshow(case_actions.Action):
    def setup(self):
        self.do_setup(dial_test.cases["Test_playshow"])
    def run(self):
        self.do_run(dial_test.cases["Test_playshow"])
    def teardown(self):
        self.do_teardown(dial_test.cases["Test_playshow"])


