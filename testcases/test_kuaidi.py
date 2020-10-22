"""
测试用例模块

"""
import os
import random
import unittest


from pack_lib.ddt import ddt, data
from common.read_excel import ReadExcel
from common.http_requests import HTTPRequest
from common.mylogger import log
from common.constant import DATA_DIR
import json



# 拼接数据文件路径
data_file_path = os.path.join(DATA_DIR, "cases.xlsx")


@ddt
class KuaidiTestCase(unittest.TestCase):
    """快递接口"""
    excel = ReadExcel(data_file_path, 'kuaidi')
    cases = excel.read_data_obj()
    http = HTTPRequest()

    @data(*cases)
    def test_case_kuaidi(self, case):

        # 登录接口用例执行的逻辑
        # 第一步：准备测试用例数据
        url = case.url
        data =case.data
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1
        headers={'Content-Type':'application/x-www-form-urlencoded'}
        # 第二步：发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url, data=data,headers=headers)
        # 获取返回的内容
        res = json.loads(response.text)
        # 第三步：比对预期结果和实际结果，断言用例是否通过
        try:
            self.assertEqual(excepted['EBusinessID'],res['EBusinessID'])
            self.assertEqual(excepted['ShipperCode'],res['ShipperCode'])
            self.assertEqual(excepted['State'],res['State'])
            self.assertEqual(excepted['Success'],res['Success'])


        except AssertionError as e:
            # 测试用例未通过
            # 获取当前用例所在行
            self.excel.write_data(row=row, column=8, value='未通过')
            log.debug('{}，该条用例执行未通过'.format(case.title))
            raise e
        else:
            # 测试用例执行通过
            self.excel.write_data(row=row, column=8, value='通过')
            log.debug('{}，该条用例执行通过'.format(case.title))

@ddt
class TishiyuTestCase(unittest.TestCase):
    """快递接口"""
    excel = ReadExcel(data_file_path, 'tishiyu')
    cases = excel.read_data_obj()
    http = HTTPRequest()

    @data(*cases)
    def test_case_kuaidi(self, case):

        # 登录接口用例执行的逻辑
        # 第一步：准备测试用例数据
        url = case.url
        data =case.data
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1
        headers={'Content-Type':'application/x-www-form-urlencoded'}
        # 第二步：发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url, data=data,headers=headers)
        # 获取返回的内容
        res = json.loads(response.text)
        # 第三步：比对预期结果和实际结果，断言用例是否通过

        try:
            # self.assertEqual(excepted['EBusinessID'],res['EBusinessID'])
            # self.assertEqual(excepted['ShipperCode'],res['ShipperCode'])
            # self.assertEqual(excepted['State'],res['State'])
            self.assertEqual(excepted['Success'],res['Success'])
            self.assertEqual(excepted['Reason'],res['Reason'])


        except AssertionError as e:
            # 测试用例未通过
            # 获取当前用例所在行
            self.excel.write_data(row=row, column=8, value='未通过')
            log.debug('{}，该条用例执行未通过'.format(case.title))
            raise e
        else:
            # 测试用例执行通过
            self.excel.write_data(row=row, column=8, value='通过')
            log.debug('{}，该条用例执行通过'.format(case.title))








