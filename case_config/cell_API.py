#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import case_config.config as config

server_IP = config.server_IP
server_port = config.server_port

u'''批量更新设备字典数据'''
Test_p0_1_insertDataByTableName = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/deviceclouddata/insertDataByTableName",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "data": [
                        1
                    ],
                    "extAttributes": {},
                    "sourceSysId": "string",
                    "tableName": "deviceAttribute",
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
                    "code": "200",
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

u'''图片列表查询'''
Test_p0_1_getFileList_test = {
    "setup": [
        "update_token",
        #'update_config_from_DB(table="id.id_schedule", whichone="lastone", item_list=[(1, "jj")])'
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/image/getFileList",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "componentName": "mdm",
                    "currentPage": 1,
                    "endTime": "TIMENOW",
                    "extAttributes": {},
                    "pageSize": 10,
                    "sourceSysId": "string",
                    "startTime": "2008-08-08 08:08:08",
                    "tableName": "mdc.base_user",
                    "targetSysId": "string",
                    "url": "string",
                    "uuid": "string"
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
                'update_config_from_resp(("Picuuid", self.resp["data"]["records"][0]["uuid"]))',
                'update_config_from_resp(("Picurl", self.resp["data"]["records"][0]["url"]))',
            ],
        },
    ],
    "teardown": [
    ],
}

u'''小区图像数据拉取'''
Test_p0_1_getPicFile_test = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/image/getPicFile",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "data": [
                        1
                    ],
                    "extAttributes": {},
                    "fileData": "string",
                    "id": "##config.Picurl##",
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

u'''供应商列表下发'''
Test_p0_1_distribute_test = {
    "setup": [
        "update_token",
        "update_config_by_randomstr(('DH_uuid', 20))"
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/provider/distribute",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "extAttributes": {},
                    "jsonStr": "[{\"category\":32,\"contact\":\"15958650802\",\"deleteFlag\":1,\"providerCode\":\"999\",\"providerName\":\"小泥鳅\",\"uuid\":\"##config.DH_uuid##\"}]",
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
                },
                "DB-match": {
                    'table': 'mdc.dm_provider',
                    'whichone': "uuid='##config.DH_uuid##'",
                    'method': '=',
                    'expect': [(0, '##config.DH_uuid##'), (2, u'小泥鳅')],
                },
            },
            "action": [
            ],
        },
    ],
    "teardown": [
    ],
}

u'''获取住户二维码'''
Test_p0_1_getResidentQrCode_test = {
    "setup": [
        "update_token",
        'update_config_from_DB(table="mdc.base_user", whichone="lastone", item_list=[(0, "user_uuid"), (1, "user_name")])',
        'update_config_from_DB(table="mdc.base_house_user_rel", whichone="lastone", item_list=[(8, "user_type")])',
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/residentQrCode/getResidentQrCode",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "extAttributes": {},
                    "residentId": "##config.user_uuid##",
                    "residentName": "##config.user_name##",
                    "residentType": "##config.user_type##",
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


u'''结构化数据抽取'''
Test_p0_1_getstructureData_test = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1: mdc.base_user",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/structureData/getstructureData",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "componentName": "mdm",
                    "currentPage": 1,
                    "endTime": "2118-03-01 06:22:02",
                    "extAttributes": {},
                    "pageSize": 1,
                    "sourceSysId": "string",
                    "startTime": "2010-03-01 06:22:02",
                    "tableName": "mdc.base_user",
                    "targetSysId": "string",
                    "url": "string",
                    "uuid": "string"
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
                },
                "DB-match": {
                },
            },
            "action": [
            ],
        },
        {
            "name": "step2: mdc.base_org",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/structureData/getstructureData",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "componentName": "mdm",
                    "currentPage": 1,
                    "endTime": "2118-03-01 06:22:02",
                    "extAttributes": {},
                    "pageSize": 1,
                    "sourceSysId": "string",
                    "startTime": "2010-03-01 06:22:02",
                    "tableName": "mdc.base_org",
                    "targetSysId": "string",
                    "url": "string",
                    "uuid": "string"
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
                },
                "DB-match": {
                },
            },
            "action": [
            ],
        },
        {
            "name": "step3: mdc.base_house_user_rel",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/structureData/getstructureData",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "componentName": "mdm",
                    "currentPage": 1,
                    "endTime": "2118-03-01 06:22:02",
                    "extAttributes": {},
                    "pageSize": 1,
                    "sourceSysId": "string",
                    "startTime": "2010-03-01 06:22:02",
                    "tableName": "mdc.base_house_user_rel",
                    "targetSysId": "string",
                    "url": "string",
                    "uuid": "string"
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
                },
                "DB-match": {
                },
            },
            "action": [
            ],
        },
        {
            "name": "step4: mdc.org_attribute",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/structureData/getstructureData",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "componentName": "mdm",
                    "currentPage": 1,
                    "endTime": "2118-03-01 06:22:02",
                    "extAttributes": {},
                    "pageSize": 1,
                    "sourceSysId": "string",
                    "startTime": "2010-03-01 06:22:02",
                    "tableName": "mdc.org_attribute",
                    "targetSysId": "string",
                    "url": "string",
                    "uuid": "string"
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
                },
                "DB-match": {
                },
            },
            "action": [
            ],
        },
        {
            "name": "step5: mdc.base_house",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/structureData/getstructureData",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "componentName": "mdm",
                    "currentPage": 1,
                    "endTime": "2118-03-01 06:22:02",
                    "extAttributes": {},
                    "pageSize": 1,
                    "sourceSysId": "string",
                    "startTime": "2010-03-01 06:22:02",
                    "tableName": "mdc.base_house",
                    "targetSysId": "string",
                    "url": "string",
                    "uuid": "string"
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

u'''接听响应'''
Test_p0_1_anser_test = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/videontercom/anser",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "callID": "string",
                    "cmdType": "accept",
                    "dstDeviceCode": '10012001171015237031',
                    "extAttributes": {},
                    "from": "string",
                    "sdp": "string",
                    "sourceSysId": "string",
                    "srcDeviceCode": "string",
                    "stateCode": "string",
                    "targetSysId": "string",
                    "to": "string"
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


u'''挂断响应'''
Test_p0_1_bye_test = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/videontercom/bye",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "callID": "string",
                    "cmdType": "bye",
                    "dstDeviceCode": "string",
                    "extAttributes": {},
                    "from": "string",
                    "sdp": "string",
                    "sourceSysId": "string",
                    "srcDeviceCode": "string",
                    "stateCode": "string",
                    "targetSysId": "string",
                    "to": "string"
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

u'''开锁响应'''
Test_p0_1_lock_test = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/videontercom/lock",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "deviceId": "string",
                    "extAttributes": {},
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


u'''获取访客二维码'''
Test_p0_1_getVisitorQrCode_test = {
    "setup": [
        "update_token",
        'update_config_from_DB(table="mdc.base_user", whichone="delete_flag=1 and name=\'测试宋艳\'", item_list=[(0, "user_uuid"), (1, "user_name")])',
        'update_config_from_DB(table="mdc.base_house_user_rel", whichone="user_uuid=\'##config.user_uuid##\'", item_list=[(0, "user_houseId"), (8, "user_type")])',
    ],
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
            "check": {
                "resp-match": {
                    "code": "200",
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


u'''删除访客二维码'''
Test_p0_1_deleteVisitorQrCode_test = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/visitorQrCode/deleteVisitorQrCode",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "extAttributes": {},
                    "qrCode": "string",
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
                    "code": "200",
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

#---------------------------------------------------
u'''临停车线上缴费费用查询'''
Test_p0_1_selectAccessCurByExample_test = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/parkinglot/selectAccessCurByExample",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "carNum": "string",
                    "extAttributes": {},
                    "sourceSysId": "string",
                    "targetSysId": "string"
                },
            },
            "check": {
                "resp-match": {
                    "code": "200",
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


u'''停车场车位锁'''
Test_p0_1_sendLockDeviceMessageToIot_test = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/parkinglot/sendLockDeviceMessageToIot",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "carportCode": "hd000005",
                    "extAttributes": {},
                    "operateType": 0,
                    "sourceSysId": "string",
                    "subDeviceID": "string",
                    "targetSysId": "string"
                },
            },
            "check": {
                "resp-match": {
                    "code": "200",
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


u'''临停车线上缴费费用更新'''
Test_p0_1_updateAccessCurByExample_test = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/parkinglot/updateAccessCurByExample",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "carNum": "string",
                    "consumeAmount": 0,
                    "consunmeRecodeMemo": "string",
                    "courtUuid": "string",
                    "extAttributes": {},
                    "favorableAmount": 0,
                    "favorableTicketNumber": "string",
                    "favorableType": 0,
                    "feeAmount": 0,
                    "feeType": 0,
                    "operatorId": "string",
                    "operatorName": "string",
                    "serialNumber": "string",
                    "sourceSysId": "string",
                    "targetSysId": "string"
                },
            },
            "check": {
                "resp-match": {
                    "code": "200",
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

#---------------------------------------------------
u'''日志文件'''
Test_p0_1_getLogFile_test = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/transferLog/getLogFile",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "currentPage": 0,
                    "extAttributes": {},
                    "filename": "string",
                    "pageSize": 0,
                    "pathid": "string",
                    "sourceSysId": "string",
                    "targetSysId": "string",
                    "totalCount": 0
                },
            },
            "check": {
                "resp-match": {
                    "code": "200",
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

u'''日志列表'''
Test_p0_1_getLogList_test = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/transferLog/getLogList",
            },
            "send": {
                "data": {
                    "businessId": "string",
                    "currentPage": 0,
                    "date": "2018-04-09T02:55:58.936Z",
                    "extAttributes": {},
                    "pageSize": 0,
                    "sourceSysId": "string",
                    "targetSysId": "string",
                    "totalCount": 0
                },
            },
            "check": {
                "resp-match": {
                    "code": "200",
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


u'''日志中转组件ip和port'''
Test_p0_1_getServiceIpAndPorts_test = {
    "setup": [
        "update_token",
    ],
    "steps": [
        {
            "name": "step1",
            "mode": {
                "protocol": ("http", 'post'),
                "url": "http://%s:%s" % (config.server_IP2, config.server_port2) + "/api/transferLog/getServiceIpAndPorts",
            },
            "send": {
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
