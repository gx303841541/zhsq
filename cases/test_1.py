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

@modify_init(casename="Test_faceswipEvent", log_dir="D:\\it\\result\\20180615_161822-test_1\\")
class Test_faceswipEvent(case_actions.Action):
    def setup(self):
        self.do_setup(test_1.Test_faceswipEvent)
    def run(self):
        self.do_run(test_1.Test_faceswipEvent)
    def teardown(self):
        self.do_teardown(test_1.Test_faceswipEvent)


@modify_init(casename="Test_patrolHandle", log_dir="D:\\it\\result\\20180615_161822-test_1\\")
class Test_patrolHandle(case_actions.Action):
    def setup(self):
        self.do_setup(test_1.Test_patrolHandle)
    def run(self):
        self.do_run(test_1.Test_patrolHandle)
    def teardown(self):
        self.do_teardown(test_1.Test_patrolHandle)


@modify_init(casename="Test_playshow", log_dir="D:\\it\\result\\20180615_161822-test_1\\")
class Test_playshow(case_actions.Action):
    def setup(self):
        self.do_setup(test_1.Test_playshow)
    def run(self):
        self.do_run(test_1.Test_playshow)
    def teardown(self):
        self.do_teardown(test_1.Test_playshow)


@modify_init(casename="Test_visitorQrcode", log_dir="D:\\it\\result\\20180615_161822-test_1\\")
class Test_visitorQrcode(case_actions.Action):
    def setup(self):
        self.do_setup(test_1.Test_visitorQrcode)
    def run(self):
        self.do_run(test_1.Test_visitorQrcode)
    def teardown(self):
        self.do_teardown(test_1.Test_visitorQrcode)


