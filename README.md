# 代码结构
该框架集成了设备模拟器，并结合录制回放工具一起实现了全链路测试的目的
main.py: 程序入口模块，python3 main.py -f xxx_test
result: 每次执行的日志文件会放在这里
cases: 程序每次生成的用例会放在这里， 然后交由py.test执行这里的用例

case_tools:
case_tools\case_maker.py: 将配置的测试用例转换为pt.test所能识别的格式
case_tools\case_runner.py： 调用第三方工具py.test执行测试
case_tools\case_actions.py：用例执行
case_tools\case_checker.py：用例检查点校验

case_config:
case_config\config.py: 全局配置文件，所要用的全局变量信息都放这里，包括后台IP信息， 数据库地址等等
case_config\door_test.py：这个是门禁组件的测试用例，作为一个测试集。新增测试用例即参考它再写一个py文件， 内容如下：


# 每个步骤支持的操作
一. setup/teardown
1. 执行API
"def2": {
    'name': "update_config_by_tuple",#API名字
    'args': ['"userID"', "'%s'" % str(time.time())],#传递给API的参数
},

2. 启动模拟器
"sim1": {
    "name": 'sim1',#模拟器名字
    'conf': "door_conf",#模拟器用的配置文件
},

3. 从数据库获取参数
"DB1": {
    'table': 'mdc.base_user',#表名
    'where': ["name=\'刘德华\'", "delete_flag=1"],#过滤条件
    'target': [(0, "user_uuid"), (1, "user_name")],#数据库第2列的值赋值给config.user_name
},

4. 从响应获取参数(teardown only)
'resp1': {
    'field': 'uuid',#body['uuid']
    'key': 'device_uuid',#config.device_uuid = body['uuid']
},


二. steps
1. mode
"mode": {
    "name": "test",#case 名字
    "protocol": ("sim1", ''),#动作所用的协议: 1)模拟器实例 2)TCP 3)http + method 4)replay
    "url": 'www.baudo.com',#only needed when http is used
},

2. action
"action": {
    "req": {#促发用例开始的动作
        "data": {
        },
        "header": {
        }
    },

    'resp1': {#获取响应消息中的参数
        'field': 'data.passWord',
        'key': 'OT_password',
    },

    "def1": {#执行API
        'name': "make_qrcode",
        'args': ['"##config.qrCode##"', '"##config.OT_password##"'],
    },
},

3. check
"resp-match": {
    "code": "00000",
},

"resp-unmatch": {
    "code": "00002",
},

"DB-match": {
    'table': 'pc.patrol_plan',#表名
    'where': ["update_time > '" + get_timestr_by_diff(seconds=-1) + "'", "plan_name='autotest'", 'delete_flag=1'],#过滤条件
    'method': '=',
    'expect': [(1, 'autotest')],#数据库第2列的值应该='autotest'
},

"sim": {
    'name': 'sim1',#模拟器名字
    'expect': [("_id_DELETE_SCHEDULE", 1)],#模拟器的属性
},
