import os
import unittest
from ddt import ddt,data,unpack

from common.constant import DATA_DIR
from common.http_requests import HTTPRequest
from common.mylogger import log
from common.read_excel import ReadExcel
from testcases.test_recharge import data_file_path


data_file_path = os.path.join(DATA_DIR, "cases.xlsx")
# @ddt
# class LoginTestCase(unittest.TestCase):
#     """登录接口"""
#     excel = ReadExcel(data_file_path, 'login')
#     cases = excel.read_data_obj()
#     http = HTTPRequest()
#
#     @data(*cases)
#     def test_case_login(self, case):
#         url = case.url
#         data = eval(case.data)
#         method = case.method
#         excepted = eval(case.excepted)
#         row = case.case_id + 1
#
#     log.info('正在请求地址{}'.format(url))
#     response = self.http.request(method=method, url=url, data=data)
#     # 获取返回的内容
#     res = response.json()
#     # 第三步：比对预期结果和实际结果，断言用例是否通过
#     try:
#         self.assertEqual(excepted, res)
#     except AssertionError as e:
#         # 测试用例未通过
#         # 获取当前用例所在行
#         self.excel.write_data(row=row, column=8, value='未通过')
#         log.debug('{}，该条用例执行未通过'.format(case.title))
#         raise e
#     else:
#         # 测试用例执行通过
#         self.excel.write_data(row=row, column=8, value='通过')
#         log.debug('{}，该条用例执行通过'.format(case.title))

@ddt
class LoginTestCase(unittest.TestCase):
    """登录接口"""
    excel = ReadExcel(data_file_path, 'login')
    cases = excel.read_data_obj()
    http = HTTPRequest()

    @data(*cases)
    def test_case_login(self, case):

        # 登录接口用例执行的逻辑
        # 第一步：准备测试用例数据
        url = case.url
        data = eval(case.data)
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1

        # 第二步：发送请求到接口，获取结果
        log.info('正在请求地址{}'.format(url))
        response = self.http.request(method=method, url=url, data=data)
        # 获取返回的内容
        res = response.json()
        # 第三步：比对预期结果和实际结果，断言用例是否通过
        try:
            self.assertEqual(excepted, res)
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