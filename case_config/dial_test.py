#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
import time

from APIs.common_APIs import get_timestr_by_diff

from . import config

cases = collections.OrderedDict()

cases['Test_faceswipEvent'] = {
    "setup": {
        "sim1": {
            "name": 'sim1',
            'conf': "door_conf",
        },
    },

    "steps": [
        {
            "mode": {
                "name": "test",
                "protocol": ("sim1", ''),
            },

            "action": {
                "req": {
                    "upload_record": 30000,
                },
            },

            "check": {
                "DB-match": {
                    'table': 'ec.ec_event_log',
                    'where': ["start_time > '" + get_timestr_by_diff(seconds=-6) + "'", "device_code='1005200958FCDBDA1000'"],
                    'method': '=',
                    'expect': [(1, 30000), (4, "人脸开门上报"), (6, '1005200958FCDBDA1000')],
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

cases['Test_patrolHandle'] = {
    "setup": {
        "def1": {
        },
    },

    "steps": [
        {
            "mode": {
                "name": "add patrol",
                "protocol": ("replay", ),
            },

            "action": {
                "req": {
                    "module": 'add_patrol.gor',
                },
            },

            "check": {
                "DB-match": {
                    'table': 'pc.patrol_plan',
                    'where': ["update_time > '" + get_timestr_by_diff(seconds=-5) + "'", "plan_name='autotest'", 'delete_flag=1'],
                    'method': '=',
                    'expect': [(1, 'autotest')],
                },
            },
        },

        {
            "mode": {
                "name": "del patrol",
                "protocol": ("replay", ),
            },

            "action": {
                "req": {
                    "module": 'add_patrol.gor -f del_patrol.gor',
                },
            },

            "check": {
                "DB-match": {
                    'table': 'pc.patrol_plan',
                    'where': ["update_time > '" + get_timestr_by_diff(seconds=-5) + "'", "plan_name='autotest'", 'delete_flag=0'],
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

cases['Test_playshow'] = {
    "setup": {
        "sim1": {
            "name": 'sim1',
            'conf': "info_conf",
        },
    },

    "steps": [
        {
            "mode": {
                "name": "add info",
                "protocol": ("replay", ),
            },

            "action": {
                "req": {
                    "module": 'add_info.gor',
                },
            },

            "check": {
                "DB-match": {
                    'table': 'id.id_schedule',
                    'where': ["update_time > '" + get_timestr_by_diff(seconds=-5) + "'", "schedule_name='autotest'", 'delete_flag=1'],
                    'method': '=',
                    'expect': [(1, 'autotest')],
                },

                "sim": {
                    'name': 'sim1',
                    'expect': [('_id_ADD_SCHEDULE', 1)],
                },
            },
        },

        {
            "mode": {
                "name": "del info",
                "protocol": ("replay", ),
            },

            "actions": {
                "req": {
                    "module": 'add_info.gor -f del_info.gor',
                },
            },

            "check": {
                "DB-match": {
                    'table': 'id.id_schedule',
                    'where': ["update_time > '" + get_timestr_by_diff(seconds=-5) + "'", "schedule_name='autotest'", 'delete_flag=0'],
                    'method': '=',
                    'expect': [(1, 'autotest')],
                },

                "sim": {
                    'name': 'sim1',
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
