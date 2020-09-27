import openpyxl


class CaseData(object):
    """测试用数据类"""

    def __init__(self, zip_obj):
        # zip对象
        for i in zip_obj:
            # 将表头作为属性，值作为属性值
            setattr(self, i[0], i[1])


class ReadExcel(object):
    """读取excel中的用例数据"""

    def __init__(self, file_name, sheet_name):
        """
        :param file_name: excel文件名
        :param sheet_name: sheet表单名
        """
        self.file_name = file_name
        self.sheet_name = sheet_name

    def open(self):
        """打开工作薄和表单"""
        # # 打开文件，返回一个工作薄对象
        self.wb = openpyxl.load_workbook(self.file_name)
        # 通过工作薄，选择表单对象
        self.sh = self.wb[self.sheet_name]

    def read_data(self):
        """读取所有用例数据"""

        # 打开文件和表单
        self.open()
        # 按行获取所有的表格对象，每一行的内容放在一个元祖中，以列表的形式返回
        rows = list(self.sh.rows)
        # 创建一个列表cases,存放所有的用例数据
        cases = []
        # 获取表头
        titles1 = [r.value for r in rows[0]]
        # 遍历其他的数据行，和表头进行打包，转换为字典，放到cases这个列表中
        for row in rows[1:]:
            # 获取该行数据
            data = [r.value for r in row]
            # 和表头进行打包，转换为字典
            case = dict(zip(titles1, data))
            cases.append(case)
        # 将读取出来的数据进行返回
        return cases

    def read_data_obj(self):
        # 打开工作簿
        self.open()
        # 创建一个空的列表，用例存放所有的用例数据
        cases = []
        # 读取表单中的数据
        rows = list(self.sh.rows)
        # 获取表头
        titles = [r.value for r in rows[0]]
        # 遍历其他的数据行，和表头进行打包，转换为字典，放到cases这个列表中
        for row in rows[1:]:
            # 获取该行数据
            data = [r.value for r in row]
            zip_obj = zip(titles, data)
            # 将每一条用例的数据，存储为一个对象
            # 通过Case这个类来创建一个对象，参数，zip_obj
            case_data = CaseData(zip_obj)
            cases.append(case_data)
        # 将包含所有用例的列表cases进从返回
        return cases

    def write_data(self, row, column, value):
        """
        :param row:  写入的行
        :param column:  写入的列
        :param value:   写入的内容
        :return:
        """
        # 打开文件
        self.open()
        # 按照传入的行、列 内容进行写入
        self.sh.cell(row=row, column=column, value=value)
        # 保存
        self.wb.save(self.file_name)


if __name__ == '__main__':
    pass
