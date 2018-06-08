#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""main
by Kobe Gong. 2018-03-19
"""

import argparse
import datetime
import decimal
import logging
import os
import random
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
from cmd import Cmd
from collections import defaultdict

import APIs.common_APIs as common_APIs
import case_config.config as config
import case_tools.case_maker as case_maker
import case_tools.case_runner as case_runner
from APIs.common_APIs import *
from basic.cprint import cprint
from basic.log_tool import MyLogger


class ArgHandle():
    def __init__(self):
        self.parser = self.build_option_parser("-" * 50)

    def build_option_parser(self, description):
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument(
            '-l', '--cmdloop',
            action='store_true',
            help='whether go into cmd loop',
        )
        parser.add_argument(
            '-f', '--file',
            dest='config_file_list',
            action='append',
            default=[],
            help='Specify config files',
        )
        return parser

    def get_args(self, attrname):
        return getattr(self.args, attrname)

    def check_args(self):
        pass

    def run(self):
        self.args = self.parser.parse_args()
        cprint.notice_p("CMD line: " + str(self.args))
        self.check_args()


# CMD loop
class MyCmd(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "APP>"

    def default(self, arg, opts=None):
        try:
            subprocess.call(arg, shell=True)
        except:
            pass

    def emptyline(self):
        pass

    def help_exit(self):
        print("Will exit")

    def do_exit(self, arg, opts=None):
        cprint.notice_p("Exit CLI, good luck!")
        sys_cleanup()
        sys.exit()


def sys_proc(action="default"):
    global thread_ids
    thread_ids = []
    for th in thread_list:
        thread_ids.append(threading.Thread(target=th[0], args=th[1:]))

    for th in thread_ids:
        th.setDaemon(True)
        th.start()


def sys_join():
    for th in thread_ids:
        th.join()


def sys_init():
    # sys log init
    global LOG
    LOG = MyLogger(os.path.abspath(sys.argv[0]).replace('py', 'log'), clevel=logging.DEBUG,
                   rlevel=logging.WARN)
    LOG.info("Let's go!!!")

    global cprint
    cprint = cprint(__name__)

    # cmd arg init
    global arg_handle
    arg_handle = ArgHandle()
    arg_handle.run()

    # multi thread
    global thread_list
    thread_list = []


def sys_cleanup():
    LOG.info("Goodbye!!!")


if __name__ == '__main__':
    sys_init()

    case_maker.clear_case_files()
    case_file_list = []
    if arg_handle.get_args('config_file_list'):
        for config_file in arg_handle.get_args('config_file_list'):
            case_file_list.append(case_maker.CaseMaker(LOG, config_file))
    else:
        for config_file in config.suite_list:
            case_file_list.append(case_maker.CaseMaker(LOG, config_file))

    case_runner.run(case_file_list)

    sys_proc()

    if arg_handle.get_args('cmdloop'):
        signal.signal(signal.SIGINT, lambda signal,
                      frame: cprint.notice_p('Exit SYSTEM: exit'))
        my_cmd = MyCmd()
        my_cmd.cmdloop()
    else:
        sys_join()
        sys_cleanup()
        sys.exit()
