#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
import time

from APIs.common_APIs import get_timestr_by_diff

from . import config

cases = collections.OrderedDict()

"""按次收费demo
steps:
1.停车场控制器入口设备car_1上报车牌开门事件（10002）
2.修改数据库车辆入场时间字段为当前时间点的前一天
3.停车场控制器出口设备car_2上报车牌开门事件（10002）
4.模拟云端调用小区平台API：临停车线上缴费费用查询接口获取缴费信息
5.比对小区端返回的缴费信息与预期费用是否一致（6分）
"""
cases['Test_pay1'] = {
    "setup": {
        "def1": {
            'name': "update_token",
            'args': [],
        },

        "sim1": {
            "name": 'sim1',
            'conf': "car_conf",
            'N': 0
        },

        "sim2": {
            "name": 'sim2',
            'conf': "car_conf",
            'N': 1
        },
    },

    "steps": [
        {
            "mode": {
                "name": "car in",
                "protocol": ("sim1", ),
            },

            "action": {
                "req": {
                    "upload_record": 10002,
                },

                "def1": {
                    'name': "set_carin_time",
                    'args': ['days=-1'， 'minutes=-5'],
                },

                "def2": {
                    'name': "mysleep",
                    'args': [1],
                },
            },
        },

        {
            "mode": {
                "name": "car out",
                "protocol": ("sim2", ),
            },

            "action": {
                "req": {
                    "upload_record": 10002,
                },
            },

            "check": {
                "sim": {
                },
            },
        },

        {
            "mode": {
                "name": "check pay",
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/parkinglot/enquiryPaymentInformation",
            },

            "action": {
                "req": {
                    "data": {
                        "businessId": "string",
                        "carNum": "辽A123456",
                        "extAttributes": {},
                        "sourceSysId": "string",
                        "spanId": "string",
                        "targetSysId": "string",
                        "traceId": {}
                    },
                    "header": {
                        "businessId": "string",
                        "charset": "string",
                        "contentType": "string",
                        "createTimestamp": 0,
                        "extAttributes": {},
                        "sourceSysId": "string",
                        "targetSysId": "string"
                    }
                },
            },

            "check": {
                "resp-match": {
                    "consumeAmount": 6,
                },
            },
        },
    ],

    "teardown": {
        "def1": {
            'name': "run_replay",
            'args': ["'-f del_car.gor'"],
        },
    },
}

"""按时收费demo
steps:
1.停车场控制器入口设备car_3上报车牌开门事件（10002）
2.修改数据库车辆入场时间字段为当前时间点的前8分钟
3.停车场控制器出口设备car_4上报车牌开门事件（10002）
4.模拟云端调用小区平台API：临停车线上缴费费用查询接口获取缴费信息
5.比对小区端返回的缴费信息与预期费用是否一致（2元）
"""
cases['Test_pay2'] = {
    "setup": {
        "def1": {
            'name': "update_token",
            'args': [],
        },

        "sim1": {
            "name": 'sim1',
            'conf': "car_conf",
            'N': 2
        },

        "sim2": {
            "name": 'sim2',
            'conf': "car_conf",
            'N': 3
        },

        "def2": {
            'name': "mysleep",
            'args': [1],
        },
    },

    "steps": [
        {
            "mode": {
                "name": "car in",
                "protocol": ("sim1", ),
            },

            "action": {
                "req": {
                    "upload_record": 10002,
                },

                "def1": {
                    'name': "set_carin_time",
                    'args': ['minutes=-8'],
                },

                "def2": {
                    'name': "mysleep",
                    'args': [1],
                },
            },
        },

        {
            "mode": {
                "name": "car out",
                "protocol": ("sim2", ),
            },

            "action": {
                "req": {
                    "upload_record": 10002,
                },
            },

            "check": {
                "sim": {
                },
            },
        },

        {
            "mode": {
                "name": "check pay",
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/parkinglot/enquiryPaymentInformation",
            },

            "action": {
                "req": {
                    "data": {
                        "businessId": "string",
                        "carNum": "辽A123456",
                        "extAttributes": {},
                        "sourceSysId": "string",
                        "spanId": "string",
                        "targetSysId": "string",
                        "traceId": {}
                    },
                    "header": {
                        "businessId": "string",
                        "charset": "string",
                        "contentType": "string",
                        "createTimestamp": 0,
                        "extAttributes": {},
                        "sourceSysId": "string",
                        "targetSysId": "string"
                    }
                },
            },

            "check": {
                "resp-match": {
                    "consumeAmount": 2 * 10 * 10,
                },
            },
        },
    ],

    "teardown": {
        "def1": {
            'name': "run_replay",
            'args': ["'-f del_car.gor'"],
        },
    },
}
