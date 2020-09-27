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
from common.do_mysql import ReadSQL
import json


# 拼接数据文件路径
data_file_path = os.path.join(DATA_DIR, "cases.xlsx")


@ddt
class LoginTestCase(unittest.TestCase):
    """登录接口"""
    excel = ReadExcel(data_file_path, 'kuaidi')
    cases = excel.read_data_obj()
    http = HTTPRequest()

    @data(*cases)
    def test_case_login(self, case):

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
class RegisterTestCase(unittest.TestCase):
    """注册接口"""
    excel = ReadExcel(data_file_path, 'register')
    cases = excel.read_data_obj()
    http = HTTPRequest()
    db = ReadSQL()

    @data(*cases)
    def test_register(self, case):
        # 第一步：准备用例数据

        # 随机生成手机号码
        phone = self.random_phone()
        # 替换动态化的参数
        case.data = case.data.replace("*phone*",phone)

        # 第二步：发送请求,获取到实际结果
        response = self.http.request(method=case.method, url=case.url, data=eval(case.data))
        res = response.json()

        # 第三步：比对预期和实际结果
        try:
            self.assertEqual(eval(case.excepted), res)
            # 判断是否需要sql校验
            # 判断是否需要进行sql校验
            if case.check_sql:
                case.check_sql = case.check_sql.replace('*phone*',phone)
                db_res = self.db.find_count(case.check_sql)
                self.assertEqual(1, db_res)

        except AssertionError as e:
            # 用例执行为通过，写入结果
            self.excel.write_data(row=case.case_id + 1, column=8, value='未通过')
            log.info('用例执行未通过')
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=case.case_id + 1, column=8, value='通过')
            log.info('用例执行通过')

    def random_phone(self):
        """随机生成手机号"""
        while True:
            phone = "13"
            for i in range(9):
                num = random.randint(1, 9)
                phone += str(num)

            # 数据库中查找该手机号是否存在
            sql = "SELECT * FROM member WHERE MobilePhone='{}';".format(phone)
            if not self.db.find_count(sql):
                return phone




