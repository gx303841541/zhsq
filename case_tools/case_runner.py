#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""case tool
   by Kobe Gong. 2017-8-25
"""

import datetime
import os
import random
import re
import shutil
import sys
import threading
import time

import APIs.common_APIs as common_APIs
from APIs.common_APIs import (my_system, my_system_full_output,
                              my_system_no_check)
from basic.cprint import cprint

#case_lock = threading.Lock()

# ATS use this to manage a testcase
CASE_STATE = ['not_start', 'ongoing', 'running', 'done']


def run1(case_file_list):
    os.system(
        r'nosetests cases -v --with-html --html-out-file=./result/result.html')


def run(case_file_list):
    os.system(
        r'py.test -q cases --html=./result/result.html')
