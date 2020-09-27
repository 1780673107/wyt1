import os
from configparser import ConfigParser
from common.constant import CONF_DIR


conf_file_path = os.path.join(CONF_DIR,'conf.ini')

class MyConfig(ConfigParser):
    """读取配置文件的类"""
    def __init__(self):
        super().__init__()
        # 初始化的时候，打开配置文件
        self.read(conf_file_path,encoding='utf8')

myconf = MyConfig()


