# -*- encoding:UTF-8 -*-
import os
import sys

suite_list = ['pay_test']

reqid = 0
work_dir = os.path.abspath(os.path.dirname(sys.argv[0]))


server_IP = '10.101.70.236'
server_port = 81

smartGW_IP = '10.101.70.247'
smartGW_port = 20001

server_IP2 = '10.101.70.236'
server_port2 = 9046

cloud_server_IP = '47.106.21.206'
cloud_server_port = 38080

login_url = "/scp-usermgmtcomponent/admin/login?username=test&password=dGVzdA=="
cloud_login_url = "/egc-cloudapicomponent/admin/login?username=test&password=dGVzdA=="


u'''小区平台UAT数据库'''
PostgreSQL1 = {
    "host": "10.101.70.238",
    "user": "hdsc_postgres",
    "password": "hdsc_postgres",
    "db": "hdsc_db",
    "port": "5432"
}

PostgreSQL = {
    "host": "10.101.70.238",
    "user": "test_zhouhanbo",
    "password": "GfD1hfVxIev",
    "db": "hdsc_db",
    "port": "5432"
}


replayPath = r'C:\\replayit\\'
devsimPath = r'C:\\testtoolsx\\'
