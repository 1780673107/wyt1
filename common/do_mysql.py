import pymysql

from common.conifg import myconf


class ReadSQL(object):
    """操作mysql的类"""
    def __init__(self):
        # 建立连接
        self.coon = pymysql.connect(
            host=myconf.get('mysql', 'host'),  # 数据库地址
            port=myconf.getint('mysql', 'port'),  # 端口
            user=myconf.get('mysql', 'user'),  # 账号
            password=myconf.get('mysql', 'password'),  # 密码
            database=myconf.get('mysql', 'database')  # 数据库名
        )
        # 创建一个游标
        self.cur = self.coon.cursor()

    def close(self):
        # 关闭游标，
        self.cur.close()

        # 断开连接
        self.coon.close()

    def find_one(self, sql):
        """查询一条数据"""
        self.coon.commit()  # 同步数据库中数据的最新状态
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_all(self, sql):
        """返回sql语句查询到的所有结果"""
        self.coon.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_count(self, sql):
        # 查询数据的条数
        self.coon.commit()
        count = self.cur.execute(sql)
        return count


