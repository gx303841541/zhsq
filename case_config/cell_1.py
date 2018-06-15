#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import case_config.config as config

u'''获取访客二维码'''
Test_p0_1_getVisitorQrCode_test = {
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
            "name": "step1",
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
                    "endTime": "2018-09-09T02:55:58.286Z",
                    "extAttributes": {},
                    "faceId": "string",
                    "facePic": "string",
                    "fingerPrint": "string",
                    "focusOnPersonnel": "string",
                    "houseAddr": "string",
                    "houseId": "##config.user_houseId##",
                    "idenNum": "string",
                    "idenType": "string",
                    "name": "string",
                    "passCode": "string",
                    "personId": "##config.user_uuid##",
                    "personName": "##config.user_name##",
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
                    "visitorUuid": "string"
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
    ],

    "teardown": {
        "def1": {
            'name': "config_dumps",
            'args': [""],
        },
    },
}
