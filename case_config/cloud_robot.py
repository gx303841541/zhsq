#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import case_config.config as config

server_IP = config.server_IP
server_port = config.server_port

u'''状态更新'''
Test_p0_1_statusUpload = {
    "setup": [
        "cloud_update_token",
        'update_config_from_DB(table="mdc.base_court", whichone="lastone", item_list=[(0, "cell_uuid")])',
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.cloud_server_IP, config.cloud_server_port) + "/api/iRobot/statusUpload",
            },
            "send": {
                "courtId": "##config.cell_uuid##",
                "time": 1521096760891,
                "data": [
                    {
                        "robot": "ZR1001",
                        "status": "R00",
                        "battery": 98,
                        "lon": 116.2333,
                        "lat": 39.2333,
                        "error": "E00",
                        "packages": [
                            {
                                "boxId": 1,
                                "name": "张三",
                                "address": "3-1-502",
                                "phone": "13999990000",
                                "boxStatus": "P01",
                                "deliveryTime": "14:25"
                            }
                        ]
                    }
                ]
            },
            "check": {
                "resp-match": {
                    "code": "00000",
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

u'''门禁交互'''
Test_p0_1_accessControl = {
    "setup": [
        "cloud_update_token",
        'update_config_from_DB(table="mdc.base_court", whichone="lastone", item_list=[(0, "cell_uuid")])',
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.cloud_server_IP, config.cloud_server_port) + "/api/iRobot/accessControl/",
            },
            "send": {
                "dialId": "71e270f6-f78b-4aad-a671-64b32a8b9c26",
                "courtId": "##config.cell_uuid##",
                "robot": "ZR1001",
                "building": "12",
                "cell": "1",
                "node": "1",
                "command": 1
            },
            "check": {
                "resp-match": {
                    "code": "00000",
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

u'''呼梯'''
Test_p0_1_callElevator = {
    "setup": [
        "cloud_update_token",
        'update_config_from_DB(table="mdc.base_court", whichone="lastone", item_list=[(0, "cell_uuid")])',
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.cloud_server_IP, config.cloud_server_port) + "/api/iRobot/callElevator/",
            },
            "send": {
                "transactionId": "UUID",
                "courtId": "##config.cell_uuid##",
                "robot": "ZR1001",
                "building": "12",
                "cell": "1",
                "node": "1",
                "currentFloor": 4,
                "moving": 2
            },
            "check": {
                "resp-match": {
                    "code": "00000",
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


u'''电梯延时关门'''
Test_p0_1_delayCloseelevator = {
    "setup": [
        "cloud_update_token",
        'update_config_from_DB(table="mdc.base_court", whichone="lastone", item_list=[(0, "cell_uuid")])',
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.cloud_server_IP, config.cloud_server_port) + "/api/iRobot/delayCloseelevator/",
            },
            "send": {
                "transactionId": "UUID",
                "courtId": "##config.cell_uuid##",
                "robot": "ZR1001",
                "building": "12",
                "cell": "1",
                "node": "1",
                "currentLift": "1",
            },
            "check": {
                "resp-match": {
                    "code": "00000",
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

u'''点亮楼层按钮'''
Test_p0_1_lightElevator = {
    "setup": [
        "cloud_update_token",
        'update_config_from_DB(table="mdc.base_court", whichone="lastone", item_list=[(0, "cell_uuid")])',
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.cloud_server_IP, config.cloud_server_port) + "/api/iRobot/lightElevator/",
            },
            "send": {
                "transactionId": "UUID",
                "courtId": "##config.cell_uuid##",
                "robot": "ZR1001",
                "building": "12",
                "cell": "1",
                "node": "1",
                "currentLift": "1",
                "floor": 1
            },
            "check": {
                "resp-match": {
                    "code": "00000",
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


u'''查询状态'''
Test_p0_1_queryElevatorStatus = {
    "setup": [
        "cloud_update_token",
        'update_config_from_DB(table="mdc.base_court", whichone="lastone", item_list=[(0, "cell_uuid")])',
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.cloud_server_IP, config.cloud_server_port) + "/api/iRobot/queryElevatorStatus/",
            },
            "send": {
                "transactionId": "UUID",
                "courtId": "##config.cell_uuid##",
                "robot": "ZR1001",
                "building": "12",
                "cell": "1",
                "node": "1",
                "currentLift": "1",
            },
            "check": {
                "resp-match": {
                    "code": "00000",
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
