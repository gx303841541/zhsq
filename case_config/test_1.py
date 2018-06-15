#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from APIs.common_APIs import get_timestr_by_diff

from . import config

Test_faceswipEvent = {
    "setup": {
        "def1": {
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
                "upload_record": 30000,
            },
            "check": {
                "DB-match": {
                    'table': 'ec.ec_event_log',
                    'where': ["start_time > '" + get_timestr_by_diff(seconds=-6) + "'", "device_code='1005200958FCDBDA1000'"],
                    'method': '=',
                    'expect': [(1, 30000), (4, "人脸开门上报"), (6, '1005200958FCDBDA1000')],
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

Test_visitorQrcode = {
    "setup": {
        "def1": {
            'name': "update_token",
            'args': [""],
        },

        "def2": {
            'name': "update_config_by_tuple",
            'args': ['"userID"', "'%s'" % str(time.time())],
        },

        "sim1": {
            "name": 'sim1',
            'conf': "door_conf",
        },

        "DB1": {
            'table': 'mdc.base_user',
            'where': ["name=\'刘德华\'", "delete_flag=1"],
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
            "name": "test",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/visitorQrCode/getVisitorQrCode",
            },
            "send": {
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
                    "endTime": "2018-07-09T02:55:58.286Z",
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

            "action": {
                'resp1': {
                    'field': 'data.passWord',
                    'key': 'OT_password',
                },

                'resp2': {
                    'field': 'data.qrCode',
                    'key': 'qrCode',
                },

                "def1": {
                    'name': "make_qrcode",
                    'args': ['"##config.qrCode##"', '"##config.OT_password##"'],
                },
            },

            "check": {
                "resp-match": {
                    "code": "00000",
                },

                "sim": {
                    'obj': 'sim1',
                    'expect': [('_CredenceType', 8), ("_credenceNo", "##config.qrCode##"), ("_userID", "##config.userID##")],
                },
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

Test_patrolHandle = {
    "setup": {
        "def1": {
        },
    },


    "steps": [
        {
            "name": "add patrol",
            "mode": {
                "protocol": ("replay", ),
            },
            "send": {
                "module": 'add_patrol.gor',
            },

            "action": {
            },

            "check": {
                "DB-match": {
                    'table': 'pc.patrol_plan',
                    'where': ["update_time > '" + get_timestr_by_diff(seconds=-1) + "'", "plan_name='autotest'", 'delete_flag=1'],
                    'method': '=',
                    'expect': [(1, 'autotest')],
                },
            },
        },

        {
            "name": "del patrol",
            "mode": {
                "protocol": ("replay", ),
            },
            "send": {
                "module": 'add_patrol.gor -f del_patrol.gor',
            },
            "check": {
                "DB-match": {
                    'table': 'pc.patrol_plan',
                    'where': ["update_time > '" + get_timestr_by_diff(seconds=-1) + "'", "plan_name='autotest'", 'delete_flag=0'],
                    'method': '=',
                    'expect': [(1, 'autotest')],
                },
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

Test_playshow = {
    "setup": {
        "sim1": {
            "name": 'sim1',
            'conf': "info_conf",
        },
    },


    "steps": [
        {
            "name": "add info",
            "mode": {
                "protocol": ("replay", ),
            },
            "send": {
                "module": 'add_info.gor',
            },

            "action": {
            },

            "check": {
                "DB-match": {
                    'table': 'id.id_schedule',
                    'where': ["update_time > '" + get_timestr_by_diff(seconds=-5) + "'", "schedule_name='autotest'", 'delete_flag=1'],
                    'method': '=',
                    'expect': [(1, 'autotest')],
                },

                "sim": {
                    'obj': 'sim1',
                    'expect': [('_id_ADD_SCHEDULE', 1)],
                },
            },
        },

        {
            "name": "del info",
            "mode": {
                "protocol": ("replay", ),
            },
            "send": {
                "module": 'add_info.gor -f del_info.gor',
            },
            "check": {
                "DB-match": {
                    'table': 'id.id_schedule',
                    'where': ["update_time > '" + get_timestr_by_diff(seconds=-5) + "'", "schedule_name='autotest'", 'delete_flag=0'],
                    'method': '=',
                    'expect': [(1, 'autotest')],
                },

                "sim": {
                    'obj': 'sim1',
                    'expect': [("_id_DELETE_SCHEDULE", 1)],
                },
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
