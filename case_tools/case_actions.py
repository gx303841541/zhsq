#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""case tool
   by Kobe Gong. 2018-4-4
"""

import datetime
import json
import logging
import os
import random
import re
import shutil
import sys
import time

import psycopg2
import requests

import APIs.common_APIs as common_APIs
from basic.log_tool import MyLogger
from case_config import config
from case_tools.case_checker import Checker
from protocol.light_devices import Dev

APIs_list = [
    'update_token',
    'update_config_from_DB',
    'update_config_from_resp',
    'update_config_by_random',
    'config_dumps',
]


class APIs(Checker):
    def update_token(self):
        self.LOG.info('update_token')
        url = "http://%s:%d/%s" % (config.server_IP,
                                   config.server_port, config.login_url)
        self.LOG.debug(url)
        header = {
            "FrontType": 'scp-admin-ui',
        }
        resp = requests.get(url, headers=header)
        try:
            token = resp.json()['data']['token']
            config.token = token
            self.LOG.debug("Get token: " + token)
        except Exception as e:
            self.LOG.error('get token fail![%s]' % (str(e)))

    def cloud_update_token(self):
        self.LOG.info('cloud_update_token')
        url = "http://%s:%d/%s" % (config.cloud_server_IP,
                                   config.cloud_server_port, config.cloud_login_url)
        self.LOG.debug(url)
        header = {
            "FrontType": 'egc-admin-ui',
        }
        resp = requests.post(url, headers=header)
        try:
            token = resp.json()['data']['token']
            config.token = token
            self.LOG.debug("Get token: " + token)
        except Exception as e:
            self.LOG.error('get token fail![%s]' % (str(e)))

    def update_config_from_DB(self, table, whichone, item_list):
        resp = self.DB_sql_send(table, whichone)
        # self.LOG.debug("get from DB: " + str(resp))
        for id, key in item_list:
            self.LOG.debug('set config.%s = "%s"' % (key, resp[id]))
            setattr(config, key, resp[id])

    def update_config_from_resp(self, *args):
        for k, v in args:
            self.LOG.debug('set config.%s = "%s"' % (k, v))
            setattr(config, k, v)

    def update_config_by_randomstr(self, *args):
        for k, v in args:
            self.LOG.debug('set config.%s = "%s"' %
                           (k, common_APIs.random_str(v)))
            setattr(config, k, common_APIs.random_str(v))

    def config_dumps(self):
        config_dict = {}
        for item in dir(config):
            if item.startswith('_') or (type(config.__dict__[item]) == type(os)):
                continue
            config_dict[item] = config.__dict__[item]
            # self.LOG.warn('%s: %s' % (item, config.__dict__[item]))
        self.LOG.info(self.convert_to_dictstr(config_dict))

    def sim_start(self, sim_conf):
        dev_LOG = MyLogger('%s.log' % (sim_conf['name']),
                           cenable=False, flevel=logging.DEBUG, fenable=True)
        self.__dict__[sim_conf['name']] = Dev(logger=dev_LOG, config_file=sim_conf['conf'],
                                              server_addr=(config.smartGW_IP, config.smartGW_port))
        self.__dict__[sim_conf['name']] .run_forever()
        time.sleep(1)
        self.LOG.warn('%s is running' % sim_conf['name'])


class Action(APIs):
    def do_setup(self, datas_dict):
        self._init_()
        req_list = []
        DB_list = []
        def_list = []
        sim_list = []
        self.LOG.info('setup start...')
        for item in datas_dict['setup']:
            if re.search(r'^req', item) and datas_dict['setup'][item]:
                req_list.append(item)
            elif re.search(r'^DB', item) and datas_dict['setup'][item]:
                DB_list.append(item)
            elif re.search(r'^def', item) and datas_dict['setup'][item]:
                def_list.append(item)
            elif re.search(r'^sim', item) and datas_dict['setup'][item]:
                sim_list.append(item)
            else:
                self.LOG.error('Unknow item: %s' % item)

        for item in (DB_list):
            self.update_config_from_DB(datas_dict['setup'][item]['table'], datas_dict['setup']
                                       [item]['where'], datas_dict['setup'][item]['target'])

        for item in sorted(def_list):
            args = ''
            for arg in datas_dict['setup'][item]["args"]:
                args += arg
            eval("self.%s(%s)" % (datas_dict['setup'][item]["name"], args))

        for item in sorted(sim_list):
            self.sim_start(datas_dict['setup'][item])

        self.LOG.info('setup end.\n\n')

    def do_run(self, datas_dict):
        if 'steps' in datas_dict:
            step_id = 0
            for step in datas_dict['steps']:
                step_id += 1
                if 'name' in step:
                    step_name = step["name"]
                else:
                    step_name = str(step_id)
                self.LOG.info('step %s start...' % (step_name))
                resp = self.send_data(
                    step['mode'], self.data_wash(step['send']))
                self.resp = resp
                self.result_check(self.data_wash(step['check']), resp)
                self.action(step['action'])
                self.LOG.info(
                    'step %s end.\n%s\n\n' % (step_name, '-' * 20))
            self.case_pass()
        else:
            self.LOG.error('"setup" config error, please check it!')
            assert False

    def do_teardown(self, datas_dict):
        self.LOG.info('teardown start...')
        resp_list = []
        DB_list = []
        def_list = []
        for item in datas_dict['teardown']:
            if re.search(r'^resp', item) and datas_dict['teardown'][item]:
                resp_list.append(item)
            elif re.search(r'^DB', item) and datas_dict['teardown'][item]:
                DB_list.append(item)
            elif re.search(r'^def', item) and datas_dict['teardown'][item]:
                def_list.append(item)

        for item in DB_list:
            self.update_config_from_DB(datas_dict['teardown'][item]['table'], datas_dict['teardown']
                                       [item]['where'], datas_dict['teardown'][item]['target'])

        for item in sorted(def_list):
            args = ''
            for arg in datas_dict['teardown'][item]["args"]:
                args += arg
            eval("self.%s(%s)" % (datas_dict['teardown'][item]["name"], args))

        for item in resp_list:
            self.update_config_from_resp(self.resp, datas_dict['teardown'][item])

        #self.LOG.debug('config info after teardown:')
        # self.config_dumps()
        self.LOG.info('teardown end.')

    def send_data(self, mode, data):
        resp = ''
        if mode['protocol'][0] == 'http':
            header = {
                "FrontType": 'egc-mobile-ui',
                "Content-Type": 'application/json',
                "Authorization": config.token,
            }
            if mode['url'].startswith('http'):
                url = mode['url']
            else:
                url = "http://%s:%d/%s" % (config.server_IP,
                                           config.server_port, mode['url'])
            self.LOG.debug(url)
            # self.LOG.debug("send headers: " + self.convert_to_dictstr(header))
            self.LOG.debug("send msg: " + self.convert_to_dictstr(data))
            if mode['protocol'][1] == "get":
                try:
                    resp = requests.get(url, headers=header, timeout=1)
                except requests.exceptions.ConnectTimeout:
                    self.LOG.warn('HTTP timeout')
                    # assert False
                else:
                    resp = resp.json()
                    self.LOG.debug(
                        "recv msg: " + self.convert_to_dictstr(resp))

            elif mode['protocol'][1] == "post":
                try:
                    resp = requests.post(url, headers=header,
                                         data=json.dumps(data), timeout=5)
                except requests.exceptions.ConnectTimeout:
                    self.LOG.warn('HTTP timeout')
                    # assert False
                else:
                    resp = resp.json()
                    self.LOG.debug(
                        "recv msg: " + self.convert_to_dictstr(resp))
            else:
                pass
        elif mode['protocol'][0] == 'tcp':
            pass
        elif mode['protocol'][0].startswith('sim'):
            sim = self.__dict__[mode['protocol'][0]]
            for item in data:
                if item == 'upload_record':
                    sim.send_msg(sim.get_upload_record(int(data['upload_record'])))
                elif item == 'upload_event':
                    sim.send_msg(sim.get_upload_event(int(data['upload_event'])))
                else:
                    self.LOG.error('Unknow msg: %s' % item)

        return resp

    def data_wash_core(self, data):
        data = re.sub(r'\'TIMENOW\'', '"%s"' % datetime.datetime.now(
        ).strftime('%Y-%m-%d %H:%M:%S'), str(data))
        m = re.findall(r'(##.*?##)', str(data))
        k = [item for item in m]
        # self.LOG.debug(str(k))
        v = [eval(item.replace('#', '')) for item in k]
        # self.LOG.debug(str(v))
        d = dict(zip(k, v))
        # self.LOG.debug(str(d))
        for d, s in d.items():
            data = data.replace(d, s)
        return data

    def data_wash(self, data):
        tmp_data = str(data)
        tmp_data = self.data_wash_core(tmp_data)
        # self.LOG.error(tmp_data)
        return eval(tmp_data)

    def action(self, actions):
        self.LOG.info('start actions...')
        for action in actions:
            if action.endswith(')'):
                self.LOG.info('action:' + "self.%s" %
                              (self.data_wash_core(action)))
                eval("self.%s" % (self.data_wash_core(action)))
            else:
                eval("self.%s()" % (self.data_wash_core(action)))
