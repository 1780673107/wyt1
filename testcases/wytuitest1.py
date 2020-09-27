import time
import unittest

from selenium import webdriver

#快递鸟登录脚本1


class kuaidi(unittest.TestCase):
    def test_kuaidiniao(self):
        driver=webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        driver.get('http://www.kdniao.com/login')
        driver.find_element_by_id('txtUserName').send_keys('15274802318')
        driver.find_element_by_id('txtPwd').send_keys('wyt5366614772')
        driver.find_element_by_xpath('//input[@class="g-btn w300 tc"]').click()
        time.sleep(2)


