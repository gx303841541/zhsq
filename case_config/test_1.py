#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import config

Test_getFileList = {
    "setup": {
        "def1": {
            'name': "update_token",
            'args': [""],
        },

        "sim1": {
            "name": 'sim1',
            'conf': "door_conf",
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
                    'table': 'ec.ec_event_log',
                    'where': 'lastone',
                    'method': '=',
                    'expect': [(1, 30001), (4, "远程开门上报"), (6, '1005200958FCDBDA1000')],
                },
            },
            "action": {
            },
        },
    ],




    "teardown": {
        "def1": {
            'name': "config_dumps",
            'args': [""],
        },
    },
}
