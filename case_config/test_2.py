#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import config

server_IP = config.server_IP
server_port = config.server_port


p0_1_getFileList_test = {
    "setup": {
        "def1": {
            'name': "update_token",
            'args': [""],
        },

        "sim1": {
            "name": 'sim1'
            'conf': "door_conf",
        },

        "DB": {
            "table": "id.id_schedule",
            "where": "delete_flag=1",
            "target": [(1, "jj")],
        },

    },

    "steps": [
        {
            "name": "test",
            "mode": {
                "protocol": ("sim1", ''),
            },
            "send": {
                "upload_record": 30001,
            },
            "check": {
                "DB-match": {
                    'table': 'id.id_schedule',
                    'where': 'lastone',
                    'method': '=',
                    'expect': (6, 'daily'),
                },
            },
            "action": {
            },
        }，
    ],



    "teardown": {
        "def1": {
            'name': "config_dumps",
            'args': [""],
        },
    },
}


p0_1_update_schedule_test = {

    "steps": [
        {
            "name": "你妹",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "/scp-informationreleaseapp/schedule/update",
            },
            "send": {
                "createUser": "admin",
                "scheduleName": "##config.scheduleName##",
                "scheduleType": "daily",
                "scheduleId": "##config.scheduleId##",
                "programNo": "1475b32258b241abbd94c84e14eb0371",
                "dailySchedule": {
                    "platspan": ["17:51:42", "18:51:45"]
                }
            },
            "check": {
                "resp-match": {
                    "code": "00000",
                },
                "resp-unmatch": {
                    "code": "00002",
                },
                "DB-match": {
                    'table': 'id.id_schedule',
                    'whichone': "uuid='##config.scheduleId##'",
                    'method': '~',
                    'expect': (7, 185145),
                },
                "DB-match1": {
                    'table': 'id.id_schedule',
                    'whichone': "uuid='##config.scheduleId##'",
                    'method': '!~',
                    'expect': (7, 185144),
                },
                "DB-match2": {
                    'table': 'id.id_schedule',
                    'whichone': 'randomone',
                    'method': 'exist',
                    'expect': 'None',
                },
            },
            "action": [

            ],
        },
    ],

}
