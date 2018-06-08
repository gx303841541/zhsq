# -*- coding: utf-8 -*-

"""common methods
by Kobe Gong 2017-8-21
use:
    methods in class CommMethod can be used by all the testcases
"""
import json
import re
import sys
import time

import APIs.common_APIs as common_APIs
import basic.framework as framework

try:
    import queue as Queue
except:
    import Queue


class CommMethod(framework.TestCase):
    # convert str or dict object to beautiful str
    def convert_to_dictstr(self, src):
        if isinstance(src, dict):
            return json.dumps(src, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)

        elif isinstance(src, str):
            return json.dumps(json.loads(src), sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)

        elif isinstance(src, bytes):
            return json.dumps(json.loads(src.decode('utf-8')), sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)

        else:
            self.LOG.error('Unknow type(%s): %s' % (src, str(type(src))))
            return None

    # just as its name implies
    def json_items_compare(self, template_dict, target):
        return self.dict_items_compare(template_dict, json.loads(target))

    # just as its name implies
    def dict_items_compare(self, template_dict, target):
        result = True
        if not isinstance(target, dict):
            self.LOG.error("target: %s is not dict instance!" % (str(target)))
            return False
        else:
            def find_item(item, target_dict):
                for key in target_dict:
                    if isinstance(target_dict[key], dict):
                        if find_item(item, target_dict[key]):
                            return True
                    if isinstance(target_dict[key], list):
                        for i in target_dict[key]:
                            if isinstance(i, dict):
                                if find_item(item, i):
                                    return True
                                else:
                                    self.LOG.warn(unicode(i))
                                    continue
                    else:
                        if key == item[0] and target_dict[key] == item[1]:
                            self.LOG.info('Found %s' % (str(item)))
                            # self.LOG.info('Found %s' % (unicode(item)))
                            return True
                        else:
                            continue
                return False

            for item in template_dict.items():
                if find_item(item, target):
                    pass
                else:
                    self.LOG.warn('Not find %s in target:\n%s' %
                                  (str(item), self.convert_to_dictstr(target)))
                    #(unicode(item), self.convert_to_dictstr(target)))
                    result = False
        return result

    # a sleep with a feedback func, if func return True, sleep will be interrupt
    def mysleep(self, timeout=1, feedback=None, *arg):
        counter = 0
        while True:
            if feedback and feedback(*arg):
                return True
            elif counter >= timeout:
                return False
            else:
                self.LOG.debug('Total %ds, %ds left...' %
                               (timeout, timeout - counter))
                counter += 1
                time.sleep(1)

    # just as its name implies
    def json_compare(self, template, target):
        return self.dict_compare(template, json.loads(target))

    # just as its name implies
    def dict_compare(self, template, target):
        if not isinstance(template, dict):
            self.LOG.error("template: %s is not dict instance!" %
                           (str(template)))
            return False

        if not isinstance(target, dict):
            self.LOG.error("target: %s is not dict instance!" % (str(target)))
            return False

        result = True
        if template == target:
            return result
        else:
            def list_print(src, dst, indent=''):
                result = True
                if len(src) != len(dst):
                    result = False

                def dict_modify(src_dict, dst_key):
                    for item in src_dict:
                        if item == dst_key and unicode(src_dict[dst_key]) != u'no_need':
                            src_dict[dst_key] = 'no_need'
                            return True
                        elif isinstance(src_dict[item], dict):
                            if dict_modify(src_dict[item], dst_key):
                                return True
                        elif isinstance(src_dict[item], list):
                            for i in src_dict[item]:
                                if isinstance(i, dict):
                                    if dict_modify(i, dst_key):
                                        return True
                        else:
                            continue
                    return False

                def find_from_dict(src_dict):
                    keys = []
                    for item in src_dict:
                        if isinstance(src_dict[item], dict):
                            keys += find_from_dict(src_dict[item])
                        elif isinstance(src_dict[item], list):
                            for i in src_dict[item]:
                                if isinstance(i, dict):
                                    keys += find_from_dict(i)
                                else:
                                    if re.match(r'no_need', unicode(src_dict[item]), re.I):
                                        keys.append(item)
                        else:
                            if re.match(r'no_need', unicode(src_dict[item]), re.I):
                                keys.append(item)
                    return keys

                keys = []
                for item in src:
                    if isinstance(item, dict) and item:
                        keys += find_from_dict(item)

                for k in keys:
                    for item in dst:
                        if isinstance(item, dict):
                            if dict_modify(item, k):
                                break

                self.LOG.info(indent + '[')
                check_list = []
                for item in sorted(list(src + dst)):
                    if item in check_list:
                        continue
                    else:
                        check_list.append(item)

                    if item in src and item in dst:
                        if isinstance(item, dict):
                            if not dict_print(item, item, indent + '  '):
                                result = False
                        else:
                            info = indent + '  ' + unicode(item)
                            self.LOG.info(info)
                    elif item in src:
                        if isinstance(item, dict):
                            if not dict_print(item, {}, indent + '  '):
                                result = False

                        elif isinstance(item, list):
                            if not dict_print(item, [], indent + '  '):
                                result = False

                        else:
                            info = indent + '  ' + unicode(item)
                            self.LOG.info(info.ljust(
                                100, '-') + 'expected only')
                            result = False
                    else:
                        if isinstance(item, dict):
                            if not dict_print({}, item, indent + '  '):
                                result = False

                        elif isinstance(item, list):
                            if not list_print([], item, indent + '  '):
                                result = False

                        else:
                            info = indent + '  ' + unicode(item)
                            self.LOG.info(info.ljust(
                                100, '-') + 'actuality only')
                            result = False
                self.LOG.info(indent + ']')
                return result

            def dict_print(src, dst, indent=''):
                result = True
                self.LOG.info(indent + '{')
                for key in sorted(list(set((src.keys() + dst.keys())))):
                    if key in src and key in dst:
                        if isinstance(src[key], dict):
                            self.LOG.info(indent + '  ' + key + ' : ')
                            if not dict_print(src[key], dst[key], indent + '  '):
                                result = False

                        elif isinstance(src[key], list):
                            if not list_print(src[key], dst[key], indent + '  '):
                                result = False

                        else:
                            info = indent + '  ' + key + \
                                ' : ' + unicode(src[key])
                            if src[key] == dst[key] or re.match(r'^no_need$', unicode(src[key]), re.I):
                                self.LOG.info(info)
                            else:
                                info += ' VS ' + unicode(dst[key])
                                self.LOG.info(info.ljust(
                                    100, '-') + 'mismatch')
                                result = False
                    elif key in src:
                        if isinstance(src[key], dict):
                            self.LOG.info(
                                (indent + '  ' + key + ' : ').ljust(100, '-') + 'expected only')
                            if not dict_print(src[key], {}, indent + '  '):
                                result = False
                        else:
                            info = indent + '  ' + key + \
                                ' : ' + unicode(src[key])
                            self.LOG.info(info.ljust(
                                100, '-') + 'expected only')
                            result = False
                    else:
                        if isinstance(dst[key], dict):
                            self.LOG.info(
                                (indent + '  ' + key + ' : ').ljust(100, '-') + 'actuality only')
                            if not dict_print({}, dst[key], indent + '  '):
                                result = False
                        else:
                            info = indent + '  ' + key + \
                                ' : ' + unicode(dst[key])
                            self.LOG.info(info.ljust(
                                100, '-') + 'actuality only')
                            result = False
                self.LOG.info(indent + '}')
                return result

            result = dict_print(template, target)
            if not result:
                self.LOG.error("template != target")

            return result
