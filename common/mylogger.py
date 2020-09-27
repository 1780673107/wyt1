import logging
from common.conifg import myconf
from common.constant import LOG_DIR
import os

# 读取配置文件中日志相关的配置项
# 读取日志收集器等级
log_level = myconf.get('log', 'log_level')
# 读取输出到控制台的等级
sh_level = myconf.get('log', 's_level')
# 读取输出到文件的等级
fh_level = myconf.get('log', 'f_level')
# 读取日志保存的文件名
name = myconf.get('log', 'filename')

# 拼接日志文件路径
file_path = os.path.join(LOG_DIR,name)

class MyLogging(object):

    def __new__(cls, *args, **kwargs):
        # 第一步：创建日志收集器对象
        my_log = logging.getLogger('my_log')
        my_log.setLevel(log_level)

        # 第二步：创建日志输出渠道
        # 输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(sh_level)
        # 输出到文件
        fh = logging.FileHandler(file_path, encoding='utf8')
        fh.setLevel(fh_level)

        # 第三步：将日志收集器和输出渠道进行绑定
        my_log.addHandler(sh)
        my_log.addHandler(fh)
        # 指定日志输出的格式
        fot = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        # 创建日志格式对象
        formatter = logging.Formatter(fot)
        # 输出格式绑定到输出渠道（给输出渠道指定输出格式）
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        # 将日志收集器进程返回
        return my_log


# 创建一个日志收集器对象
log = MyLogging()
