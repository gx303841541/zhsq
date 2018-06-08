#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""ATS socket
   by Kobe Gong. 2018-3-21
"""

import datetime
import json
import os
import random
import re
import select
import socket
import sys
import threading
import time

import requests

import APIs.common_APIs as common_APIs
from APIs.common_APIs import protocol_data_printB
from basic.log_tool import MyLogger

r = requests.get('https://github.com/timeline.json')


>> > r = requests.post("http://httpbin.org/post")
>> > r = requests.put("http://httpbin.org/put")
>> > r = requests.delete("http://httpbin.org/delete")
>> > r = requests.head("http://httpbin.org/get")
>> > r = requests.options("http://httpbin.org/get")


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)


url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}


r = requests.post(url, data=json.dumps(payload), headers=headers)
