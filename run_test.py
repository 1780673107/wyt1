
import unittest
import os
from HTMLTestRunnerNew import HTMLTestRunner
from common.mylogger import log
from common.constant import CASES_DIR,REPORT_DIR


log.info('-------------------开启测试运行程序--------------')

# 第一步创建测试套件
suite = unittest.TestSuite()


# 第二步 将用例添加到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASES_DIR))

# 拼接测试报告的路径
report_file_path = os.path.join(REPORT_DIR,'report.html')

# 第三步：执行用例,生成测试报告

with open(report_file_path,"wb") as fb:
    runner = HTMLTestRunner(stream=fb,
                            verbosity=2,
                            title='快递鸟接口项目',
                            description="快递鸟接口项目",
                            tester="wyt")

    runner.run(suite)

log.info('----------本次所有用例执行完毕---------------------')


