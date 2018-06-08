#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import case_config.config as config

u'''机器人下发请求到门禁组件'''
Test_p0_1_sendOpenDoor = {
    "setup": [
        "update_token",
        'update_config_from_DB(table="mdc.base_court", whichone="lastone", item_list=[(0, "cell_uuid")])',
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/robot/sendOpenDoor",
            },
            "send": {
                "data": {
                    "building": "10",
                    "businessId": "string",
                    "cell": "1",
                    "command": 0,
                    "courtId": "##config.cell_uuid##",
                    "extAttributes": {},
                    "node": "1",
                    "robot": "xjj",
                    "sourceSysId": "string",
                    "targetSysId": "string"
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
            "check": {
                "resp-match": {
                    "code": "00000",
                    "message": "success"
                },
                "DB-match": {
                },
            },
            "action": [
            ],
        },
    ],
    "teardown": [
    ],
}

u'''将电梯呼到所在楼层'''
Test_p0_1_callLift = {
    "setup": [
        "update_token",
        'update_config_from_DB(table="mdc.base_court", whichone="lastone", item_list=[(0, "cell_uuid")])',
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/robot/callLift",
            },
            "send": {
                "data": {
                    "building": "10",
                    "businessId": "string",
                    "cell": "1",
                    "courtId": "##config.cell_uuid##",
                    "currentFloor": 1,
                    "currentLift": "string",
                    "delay": 0,
                    "extAttributes": {},
                    "floor": 0,
                    "moving": 0,
                    "node": "101",
                    "robot": "ZR1001",
                    "sourceSysId": "string",
                    "targetSysId": "string",
                    "transactionId": "string"
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
            "check": {
                "resp-match": {
                    "code": "00000",
                    "message": "success"
                },
                "DB-match": {
                },
            },
            "action": [
            ],
        },
    ],
    "teardown": [
    ],
}


u'''电梯延时关门指令'''
Test_p0_1_keepOpen = {
    "setup": [
        "update_token",
        'update_config_from_DB(table="mdc.base_court", whichone="lastone", item_list=[(0, "cell_uuid")])',
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/robot/keepOpen",
            },
            "send": {
                "data": {
                    "building": "10",
                    "businessId": "string",
                    "cell": "1",
                    "courtId": "##config.cell_uuid##",
                    "currentFloor": 0,
                    "currentLift": "string",
                    "delay": 0,
                    "extAttributes": {},
                    "floor": 1,
                    "moving": 1,
                    "node": "101",
                    "robot": "string",
                    "sourceSysId": "string",
                    "targetSysId": "string",
                    "transactionId": "string"
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
            "check": {
                "resp-match": {
                    "code": "00000",
                    "message": "success"
                },
                "DB-match": {
                },
            },
            "action": [
            ],
        },
    ],
    "teardown": [
    ],
}


u'''点亮目的楼层按钮'''
Test_p0_1_lightUp = {
    "setup": [
        "update_token",
        'update_config_from_DB(table="mdc.base_court", whichone="lastone", item_list=[(0, "cell_uuid")])',
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/robot/lightUp",
            },
            "send": {
                "data": {
                    "building": "10",
                    "businessId": "string",
                    "cell": "1",
                    "courtId": "##config.cell_uuid##",
                    "currentFloor": 0,
                    "currentLift": "string",
                    "delay": 0,
                    "extAttributes": {},
                    "floor": 0,
                    "moving": 0,
                    "node": "101",
                    "robot": "string",
                    "sourceSysId": "string",
                    "targetSysId": "string",
                    "transactionId": "string"
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
            "check": {
                "resp-match": {
                    "code": "00000",
                    "message": "success"
                },
                "DB-match": {
                },
            },
            "action": [
            ],
        },
    ],
    "teardown": [
    ],
}


u'''主动发起查询电梯状态请求'''
Test_p0_1_stateQuery = {
    "setup": [
        "update_token",
        'update_config_from_DB(table="mdc.base_court", whichone="lastone", item_list=[(0, "cell_uuid")])',
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/robot/stateQuery",
            },
            "send": {
                "data": {
                    "building": "10",
                    "businessId": "string",
                    "cell": 1,
                    "courtId": "##config.cell_uuid##",
                    "currentFloor": 2,
                    "currentLift": "1",
                    "delay": 0,
                    "extAttributes": {},
                    "floor": 1,
                    "moving": 3,
                    "node": "101",
                    "robot": "ZR1001",
                    "sourceSysId": "string",
                    "targetSysId": "string",
                    "transactionId": "string"
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
            "check": {
                "resp-match": {
                    "code": "00000",
                    "message": "success"
                },
                "DB-match": {
                },
            },
            "action": [
            ],
        },
    ],
    "teardown": [
    ],
}
