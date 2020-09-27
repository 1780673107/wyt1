
import os
import time

from common.operate_config import conf
from selenium.common.exceptions import *
from common.constant import SCREEN_SHOT_DIR
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    """页面通用方法"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素封装
    def wait_element(self, locator, timeout=10, frequency=0.2):
        """自定义等待元素出现"""
        wait_time = 0
        while wait_time < timeout:
            try:
                element = self.driver.find_element(*locator)
                time.sleep(frequency)
                return element
            except NoSuchElementException:
                time.sleep(frequency)
                wait_time += frequency

        self.screen_shot()
        raise NoSuchElementException

    def wait_element_presence(self, locator, timeout=10, frequency=0.2):
        try:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency).until(
                ec.presence_of_element_located(locator))
        except TimeoutException:
            self.screen_shot()
            raise TimeoutException

    def wait_all_elements_presence(self, locator, timeout=10, frequency=0.2):
        try:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency).until(
                ec.presence_of_all_elements_located(locator))
        except TimeoutException:

            self.screen_shot()
            raise TimeoutException

    def wait_element_not_presence(self, locator, timeout=10, frequency=0.2):
        try:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency).until_not(
                ec.presence_of_element_located(locator))
        except TimeoutException:
            self.screen_shot()
            raise TimeoutException

    def wait_element_visibility(self, locator, timeout=10, frequency=0.2):
        try:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency).until(
                ec.visibility_of_element_located(locator))
        except TimeoutException:
            self.screen_shot()
            raise TimeoutException

    def wait_element_not_visibility(self, locator, timeout=10, frequency=0.2):
        try:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency).until_not(
                ec.visibility_of_element_located(locator))
        except TimeoutException:
            self.screen_shot()
            raise TimeoutException

    def wait_element_clickable(self, locator, timeout=10, frequency=0.2):
        try:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency).until(
                ec.element_to_be_clickable(locator))
        except TimeoutException:
            self.screen_shot()
            raise TimeoutException

    def wait_element_not_clickable(self, locator, timeout=10, frequency=0.2):
        try:
            return WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency).until_not(
                ec.element_to_be_clickable(locator))
        except TimeoutException:
            self.screen_shot()
            raise TimeoutException

    # 鼠标操作封装
    def right_click(self, on_element=None):
        return ActionChains(self.driver).context_click(on_element=on_element).perform()

    def move_to(self, to_element):
        return ActionChains(self.driver).move_to_element(to_element=to_element).perform()

    def move_to_and_click(self, to_element):
        return ActionChains(self.driver).move_to_element(to_element=to_element).click().perform()

    # 截图封装
    def screen_shot(self):
        screen_shot_name = time.strftime("%Y%m%d%H%M") + ".png"
        screen_shot_file_path = os.path.join(SCREEN_SHOT_DIR,
                                             conf.get("screenshot", "screen_shot_dir_name"),
                                             screen_shot_name)
        self.driver.save_screenshot(screen_shot_file_path)

    # 键盘操作封装
    def keyboard_enter(self, element):
        return element.send_keys(Keys.ENTER)

    # 上传文件封装
    def input_upload_file(self, element, file_name):
        return element.send_keys(file_name)
