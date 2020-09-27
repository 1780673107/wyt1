import time
import unittest


from selenium import webdriver

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "unittest_百度搜索")
        print(driver.title)
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        print(now)
    def test_kuaidiniao(self):
        driver=self.driver
        driver.get('http://www.kdniao.com/login')
        driver.find_element_by_id('txtUserName').send_keys('15274802318')
        driver.find_element_by_id('txtPwd').send_keys('wyt5366614772')
        driver.find_element_by_xpath('//input[@class="g-btn w300 tc"]').click()
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()

