
import os
import unittest
import decimal

from pack_lib.ddt import ddt, data
from common.read_excel import ReadExcel
from common.constant import DATA_DIR
from common.http_requests import HTTPSession
from common.mylogger import log
from common.do_mysql import ReadSQL

data_file_path = os.path.join(DATA_DIR, 'cases.xlsx')


@ddt
class RechargeTestCase(unittest.TestCase):
    """充值接口"""
    excel = ReadExcel(data_file_path, 'recharge')
    cases = excel.read_data_obj()
    http = HTTPSession()
    db = ReadSQL()

    @data(*cases)
    def test_recharge(self, case):
        # 第一步：准备用例数据
        if case.check_sql:
            # 获取充值用例执行之后的余额
            start_money = self.db.find_one(case.check_sql)[0]
            print('充值之前用户的余额为{}'.format(start_money))

        # 第二步 发送请求，获取结果
        response = self.http.request(method=case.method, url=case.url, data=eval(case.data))
        res = response.json()
        res_code = res['code']
        # 第三步 比对预期和实际结果

        try:
            self.assertEqual(str(case.excepted_code), res_code)
            if case.check_sql:
                # 获取充值用例执行之后的余额
                end_money = self.db.find_one(case.check_sql)[0]
                print('充值之后用户的余额为{}'.format(end_money))

                # 获取本次充值的金额
                money = eval(case.data)['amount']
                money = decimal.Decimal(str(money))
                print('本次充值的金额{}'.format(money))
                # 获取数据库变化的金额

                change_money = end_money - start_money
                self.assertEqual(money, change_money)


        except AssertionError as e:
            # 用例执行未通过
            self.excel.write_data(row=case.case_id + 1, column=8, value='未通过')
            log.info('{}:用例执行未通过'.format(case.title))
            log.exception(e)
            raise e
        else:
            # 用例执行通过
            self.excel.write_data(row=case.case_id + 1, column=8, value='通过')
            log.info('{}:用例执行通过'.format(case.title))


@ddt
class WithdrawTestCase(unittest.TestCase):
    """取现接口"""
    excel = ReadExcel(data_file_path, 'withdraw')
    cases = excel.read_data_obj()
    http = HTTPSession()
    db = ReadSQL()

    @data(*cases)
    def test_withdraw(self, case):
        # 第一步：准备用例数据
        if case.check_sql:
            # 获取充值用例执行之后的余额
            start_money = self.db.find_one(case.check_sql)[0]
            print('充值之前用户的余额为{}'.format(start_money))

        # 第二步 发送请求，获取结果
        response = self.http.request(method=case.method, url=case.url, data=eval(case.data))
        res = response.json()
        res_code = res['code']
        # 第三步 比对预期和实际结果

        try:
            self.assertEqual(str(case.excepted_code), res_code)
            if case.check_sql:
                # 获取充值用例执行之后的余额
                end_money = self.db.find_one(case.check_sql)[0]
                print('充值之后用户的余额为{}'.format(end_money))

                # 获取本次取现的金额
                money = eval(case.data)['amount']
                money = decimal.Decimal(str(money))
                print('本次充值的金额{}'.format(money))
                # 获取数据库变化的金额
                change_money = start_money -end_money
                self.assertEqual(money, change_money)


        except AssertionError as e:
            # 用例执行未通过
            self.excel.write_data(row=case.case_id + 1, column=8, value='未通过')
            log.info('{}:用例执行未通过'.format(case.title))
            log.exception(e)
            raise e
        else:
            # 用例执行通过
            self.excel.write_data(row=case.case_id + 1, column=8, value='通过')
            log.info('{}:用例执行通过'.format(case.title))


