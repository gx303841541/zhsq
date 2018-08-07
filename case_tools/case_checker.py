#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""case tool
   by Kobe Gong. 2018-4-4
"""

import datetime
import json
import os
import random
import re
import shutil
import sys
import threading
import time

import psycopg2
import requests

import APIs.common_APIs as common_APIs
import APIs.common_methods as common_methods
from case_config import config


class Checker(common_methods.CommMethod):
    def result_check(self, check_dict, resp):
        self.LOG.info('start result_check...')
        for item in check_dict:
            if item.startswith('resp-match') and check_dict[item]:
                self.LOG.info("check resp match...")
                self.resp_match_check(check_dict[item], resp)

            elif item.startswith('resp-unmatch') and check_dict[item]:
                self.LOG.info("check resp unmatch...")
                self.resp_unmatch_check(check_dict[item], resp)

            elif item.startswith('DB-match') and check_dict[item]:
                self.LOG.info("check DB match...")
                self.DB_match_check(check_dict[item])

            elif item.startswith('sim') and check_dict[item]:
                self.LOG.info("check sim match...")
                self.sim_para_check(check_dict[item])

            else:
                self.LOG.warn(
                    'More check point will be do in the feature![%s]' % item)
        self.LOG.info('stop result_check...')

    def sim_para_check(self, check_dict):
        result = True
        sim = self.__dict__[check_dict['obj']]
        for k, v in check_dict['expect']:
            dst = sim.__dict__
            k_list = k.split('.')
            for i in k_list:
                dst = dst[i]
            if dst == v:
                self.LOG.info("%s = %s" % (dst, v))
            else:
                self.LOG.error("%s != %s" % (dst, v))
                result = False
        assert result

    def resp_match_check(self, expect_resp, resp):
        result = self.dict_items_compare(expect_resp, resp)
        assert result

    def resp_unmatch_check(self, expect_resp, resp):
        result = self.dict_items_compare(expect_resp, resp)
        assert not result

    def DB_match_check(self, expect_DB):
        result = True
        if len(expect_DB):
            pass
        else:
            return

        whichone = ''
        for item in expect_DB['where']:
            if whichone:
                whichone += ' and '
            whichone += item

        resp = self.DB_sql_select(expect_DB['table'], whichone)
        if resp:
            for (id, value) in expect_DB['expect']:
                if expect_DB['method'] == '=':
                    if str(resp[id]) == str(value):
                        self.LOG.info("%s == %s" % (resp[id], value))
                    else:
                        self.LOG.error("%s != %s" % (resp[id], value))
                        result = False

                elif expect_DB['method'] == '!=':
                    if resp[id] != value:
                        self.LOG.info("%s != %s" % (resp[id], value))
                    else:
                        self.LOG.error("%s == %s" % (resp[id], value))
                        result = False

                elif expect_DB['method'] == '~':
                    if re.search(r'%s' % str(value), str(resp[id])):
                        self.LOG.info("%s ~ %s" % (resp[id], value))
                    else:
                        self.LOG.error("%s !~ %s" % (resp[id], value))
                        result = False

                elif expect_DB['method'] == '!~':
                    if not re.search(r'%s' % str(value), str(resp[id])):
                        self.LOG.info("%s !~ %s" % (resp[id], value))
                    else:
                        self.LOG.error("%s ~ %s" % (resp[id], value))
                        result = False

                elif expect_DB['method'] == 'exist':
                    pass

                else:
                    self.LOG.error("Unknow method: %s!" %
                                   (expect_DB['method']))
                    result = False
        else:
            if expect_DB['method'] == 'unexist':
                pass
            else:
                self.LOG.error("%s:%s unexist!" %
                               (expect_DB['table'], expect_DB['where']))
                result = False
        assert result

    def DB_query(self, cmd):
        if not hasattr(self, 'cur'):
            try:
                self.cxn = psycopg2.connect(
                    database=config.PostgreSQL['db'], user=config.PostgreSQL['user'], password=config.PostgreSQL['password'], host=config.PostgreSQL['host'], port=config.PostgreSQL['port'])
                self.cur = self.cxn.cursor()
            except psycopg2.OperationalError as er:
                self.LOG.error('connect to DB error!')
                return
        self.LOG.info('exec SQL:' + cmd)
        try:
            self.cur.execute(cmd)
            self.cxn.commit()
            return self.cur.fetchall()
        except psycopg2.ProgrammingError as e:
            self.LOG.warn('SQL error:' + str(e))
            return ''

    def DB_close(self):
        self.cur.close()
        self.cxn.close()

    def DB_sql_select(self, table, whichone):
        resp = self.DB_query(
            'select * from %s where %s;' % (table, whichone))
        if resp:
            resp = resp[0]
        self.LOG.debug("get from DB: " + str(resp))
        return resp

    def DB_sql_set(self, table, set, whichone):
        resp = self.DB_query(
            'update %s set %s where %s;' % (table, set, whichone))
        if resp:
            resp = resp[0]
        self.LOG.debug("get from DB: " + str(resp))
        return resp

    def mysleep(self, timeout=1, feedback=None, *arg):
        counter = 0
        while True:
            if feedback and feedback(*arg):
                return True
            elif counter >= timeout:
                return False
            else:
                self.LOG.debug('Total %ds, %ds left...' %
                               (timeout, timeout - counter))
                counter += 1
                time.sleep(1)
