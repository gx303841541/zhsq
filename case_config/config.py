# -*- encoding:UTF-8 -*-
import os
import sys

suite_list = ['test_1']

reqid = 0
work_dir = os.path.abspath(os.path.dirname(sys.argv[0]))


server_IP = '192.168.0.236'
server_port = 81

smartGW_IP = '192.168.0.247'
smartGW_port = 20001

server_IP2 = '192.168.0.236'
server_port2 = 9046

cloud_server_IP = '47.106.21.206'
cloud_server_port = 38080

login_url = "/scp-usermgmtcomponent/admin/login?username=test&password=dGVzdA=="
cloud_login_url = "/egc-cloudapicomponent/admin/login?username=test&password=dGVzdA=="


u'''小区平台UAT数据库'''
PostgreSQL = {
    "host": "192.168.0.238",
    "user": "hdsc_postgres",
    "password": "hdsc_postgres",
    "db": "hdsc_db",
    "port": "5432"
}

TestTime = 100 * 60 * 60  # 测试时间 100 小时 * 60分钟 * 60秒

replayPath = r'C:\\httpapi-master\\'
