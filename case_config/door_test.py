#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
import time

from APIs.common_APIs import get_timestr_by_diff

from . import config

cases = collections.OrderedDict()

cases['Test_cardStorage'] = {
    "setup": {

    },

    "steps": [
        {
            "mode": {
                "name": "add card",
                "protocol": ("replay", ),
            },

            "action": {
                "req": {
                    "module": 'add_card.gor',
                },
            },

            "check": {
                "DB-match": {
                    'table': 'cm.card_master',
                    'where': ["update_time > '" + get_timestr_by_diff(seconds=-5) + "'", "owner_name='自动化1'", "card_status='USED'", 'delete_flag=1', "unique_code='AABbCCdd'"],
                    'method': '=',
                    'expect': [(2, 'IC')],
                },
            },
        },

        {
            "mode": {
                "name": "del card",
                "protocol": ("replay", ),
            },

            "action": {
                "req": {
                    "module": 'del_card.gor',
                },
            },

            "check": {
                "DB-match": {
                    'table': 'cm.card_master',
                    'where': ["update_time > '" + get_timestr_by_diff(seconds=-5) + "'", "owner_name='自动化1'", "unique_code='AABbCCdd'", "card_status='RETURNED'"],
                    'method': '=',
                    'expect': [(2, 'IC')],
                },
            },
        },
    ],

    "teardown": {

    },
}

cases['Test_deviceGroup'] = {
    "setup": {

    },

    "steps": [
        {
            "mode": {
                "name": "add group",
                "protocol": ("replay", ),
            },

            "action": {
                "req": {
                    "module": 'add_autotest_group3.gor',
                },
            },

            "check": {
                "DB-match": {
                    'table': 'acc.acc_device_group',
                    'where': ["update_time > '" + get_timestr_by_diff(seconds=-1) + "'", "group_name='autotest_group3'", 'delete_flag=1'],
                    'method': '=',
                    'expect': [(1, 'autotest_group3')],
                },
            },
        },

        {
            "mode": {
                "name": "del group",
                "protocol": ("replay", ),
            },

            "action": {
                "req": {
                    "module": 'del_autotest_group3.gor',
                },
            },

            "check": {
                "DB-match": {
                    'table': 'acc.acc_device_group',
                    'where': ["update_time > '" + get_timestr_by_diff(seconds=-1) + "'", "group_name='autotest_group3'", 'delete_flag=0'],
                    'method': '=',
                    'expect': [(1, 'autotest_group3')],
                },
            },
        },
    ],

    "teardown": {

    },
}

cases['Test_permission_download'] = {
    "setup": {
        "sim1": {
            "name": 'sim1',
            'conf': "door_conf",
            'N': 1
        },

        "DB1": {
            'table': 'mdc.base_user',
            'where': ["name=\'自动化2\'", "delete_flag=1"],
            'target': [(0, "user_uuid"), (1, "user_name")],
        },
    },

    "steps": [
        {
            "mode": {
                "name": "add permission",
                "protocol": ("replay", ),
            },

            "action": {
                "req": {
                    "module": 'add_auth.gor',
                },

                "def": {
                    'name': "mysleep",
                    'args': [2],
                },
            },

            "check": {
                "sim": {
                    'obj': 'sim1',
                    'expect': [('_CredenceType.7', "group1/M00/50/AF/CmVG9ltET1KAC0DeAACFxda1h7E249.jpg"), ('_CredenceType.6', "MzAxJ3ERFkiMdoSNJViMaoiNJlicfpWpFViM6LSZFmiEgKSJJCis1b0ZFWiU29plJHicyOWpJmh4E8hhFXiE4OkhFWiU1WY9FUisaHSBFVik6KO9FkiEDM/ZFTiFa7SVFEigVXqBJDiw2OCtFdh4Y7VRJHiQS+lpFZiAYfIJFmhpZQaSFVh41/cBJCigTwxmJWh41Q7KJEiASBTqJTiJ6iSiJaiQSDaKFchwPEX+Fah4MVKWFGh5vFlqJoiQJGg2FWhwNjpVJliACkqpFYiYbValFCio1VPdFXigBFOhFkigglc5JTig4ZQNJGigVwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABMADCURYIIJ4CVWIdHKE2FIJgGhmRFj+WIwkX4G26N2IhIlCtVCGkACug5rDlMSMeEUZU9XAkHCFdfQajIhlA9VBE8hwe4X1TF3MgJCB8iYXwKhmgXVNmgkspwYSHtPAuHYGerxRiUCMgFqRgQB4u0aSF1fQuOKCBNOMRIycgB2KWYicJkLaAAAAAAAAAA="), ('_CredenceType.2', "77885511")],
                },

                "DB-match1": {

                },

            },
        },

        {
            "mode": {
                "name": "del permission",
                "protocol": ("replay", ),
            },

            "action": {
                "req": {
                    "module": 'del_auth.gor ',
                },

                "def": {
                    'name': "mysleep",
                    'args': [2],
                },
            },

            "check": {
                "sim": {
                    'obj': 'sim1',
                    'expect': [('_CredenceType.7', ""), ('_CredenceType.6', ""), ('_CredenceType.2', ""), ],
                },

                "DB-match1": {

                },

                "DB-match2": {

                },
            },
        },
    ],

    "teardown": {
    },
}

cases['Test_visitorQrcode'] = {
    "setup": {
        "def1": {
            'name': "update_token",
            'args': [],
        },

        "def2": {
            'name': "update_config_by_tuple",
            'args': ["'userID'", "'%s'" % str(time.time())],
        },

        "sim1": {
            "name": 'sim1',
            'conf': "door_conf",
        },

        "DB1": {
            'table': 'mdc.base_user',
            'where': ["name=\'自动化1\'", "delete_flag=1"],
            'target': [(0, "user_uuid"), (1, "user_name")],
        },

        "DB2": {
            'table': 'mdc.base_house_user_rel',
            'where': ["user_uuid=\'##config.user_uuid##\'", "delete_flag=1"],
            'target': [(0, "user_houseId"), (8, "user_type")],
        },
    },

    "steps": [
        {
            "mode": {
                "name": "test",
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/visitorQrCode/getVisitorQrCode",
            },

            "action": {
                "req": {
                    "data": {
                        "businessId": "string",
                        "cardId": "string",
                        "cloudPic": [
                            -1, 2, 3, 4, 5, 5, 6, 74
                        ],
                        "company": "string",
                        "courtUuid": "string",
                        "createTime": "2018-06-04T00:34:58.286Z",
                        "createUser": "string",
                        "currentFaceId": "string",
                        "currentFacePic": "string",
                        "currentFingerPrint": "string",
                        "currentLadderFlag": "string",
                        "deleteFlag": 0,
                        "effectCount": 10,
                        "endTime": "2048-07-09T02:55:58.286Z",
                        "extAttributes": {},
                        "faceId": "string",
                        "facePic": "string",
                        "fingerPrint": "string",
                        "focusOnPersonnel": "string",
                        "houseAddr": "string",
                        "houseId": "##config.user_houseId##",
                        "idenNum": "string",
                        "idenType": "string",
                        "name": "XJJ",
                        "passCode": "string",
                        "personId": "##config.user_uuid##",
                        "personName": u"##config.user_name##",
                        "personType": "##config.user_type##",
                        "phone": "string",
                        "plateNum": "string",
                        "qrCode": "string",
                        "reasonType": "string",
                        "recordSum": 5,
                        "sex": "string",
                        "sourceSysId": "string",
                        "startTime": "2018-06-04T00:55:58.286Z",
                        "targetSysId": "string",
                        "updateTime": "2018-06-04T00:55:58.286Z",
                        "updateUser": "string",
                        "uuid": "string",
                        "visitorCnt": 0,
                        "visitorType": "4",
                        "visitorUuid": "##config.userID##",
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

                'resp1': {
                    'field': 'data.passWord',
                    'key': 'OT_password',
                },

                'resp2': {
                    'field': 'data.qrCode',
                    'key': 'qrCode',
                },

                "def": {
                    'name': "mysleep",
                    'args': [2],
                },

                "def1": {
                    'name': "make_qrcode",
                    'args': ["'##config.qrCode##'", "'##config.OT_password##'"],
                },
            },

            "check": {
                "resp-match": {
                    "code": "00000",
                },

                "sim": {
                    'obj': 'sim1',
                    'expect': [('_CredenceType.8', "##config.qrCode##"), ("_userID", "##config.userID##")],
                },

                "sim2": {
                    'obj': 'sim1',
                    'expect': [('_CredenceType.11', "##config.OT_password##"), ("_userID", "##config.userID##")],
                },
            },
        },
    ],

    "teardown": {
        "def1": {
            'name': "config_dumps",
            'args': [],
        },
    },
}
