from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import xlwt

driver = webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')  # 创建一个chrome实例
driver.get("https://www.lagou.com/")  # 传入网站


# 网页爬取函数
# 主要负责解决页面弹窗处理功能
# 招聘信息的输入和也面的切换
# 将HTML提出并且调用解析函数进行信息提取
def getHtml():
    info = []  # 存放信息列表
    time.sleep(0.5)
    # 由于会弹出一个定位选择框，所以要进行选择一些，否则下面无法进行
    try:
        if driver.find_element_by_id("cboxLoadedContent"):
            driver.find_element_by_id("cboxClose").click()
    except:
        pass
    time.sleep(0.5)
    # 找出输入框位置并且输入招聘关键词
    inpText = driver.find_element_by_id("search_input")
    inpText.send_keys("自动化测试")
    driver.find_element_by_id("search_button").click()
    time.sleep(1)

    # 处理弹出广告
    try:
        if driver.find_element_by_class_name("body-box"):
            driver.find_element_by_class_name("body-btn").click()
    except:
        pass

    count = 1
    # 第一页
    try:
        html = driver.page_source
        html = str(html).replace(u"\u2002", "").replace(u"\xa9", "")
        parse(html, info)
        print("成功爬取第" + str(count) + "页")
        count += 1
    except:
        print("Failed to get page " + str(count))
        count += 1

    # 获取第二页到尾页
    panduan = 1
    while panduan == 1:
        if count <= 30:
            driver.find_element_by_class_name("pager_next ").click()
            time.sleep(2)
            html = driver.page_source
            html = str(html).replace(u"\u2002", "").replace(u"\xa9", "")
            parse(html, info)
            print("成功爬取第" + str(count) + "页")
            count += 1
        else:
            panduan = 0
            print("爬虫程序执行完成")

    saveData(info)  # 调用数据保存函数进行数据保存
    driver.close()  # 关闭浏览器页面


# 信息提取函数
# 主要将信息进行解析提取
def parse(html, infoList):
    soup = BeautifulSoup(html, "lxml")

    try:
        # 由于每一页只有14个招聘信息，所以要使用循环来给每一个li的属性"data-index赋值
        # 因为每个招聘信息的li标签都没有相同的属性值，所以只能这样子了
        a = 1
        while a <= 14:
            ul = soup.find("ul", class_='item_con_list').find_all_next("li", {"data-index": str(a)})
            for li in ul:
                # 岗位名称
                try:
                    name = li.find("a", class_="position_link").find_next("h3").text
                except:
                    name = " "

                # 地址
                try:
                    address = li.find("span", class_='add').text
                    address = str(address).replace("[", "").replace("]", "")
                except:
                    address = " "

                try:
                    text = li.find("div", class_='li_b_l').text

                    # 提取学历要求,因为在一起提取是提取不了，所以学历只能另外提取
                    education = re.findall(r"(大专|本科|硕士|博士|不要求|不限)", text)
                    if len(education) >= 1:
                        education = education[0]
                    else:
                        education = " "

                    # 提取薪资,经验要求
                    text = re.findall(r"(.*?)\n(.*?)/", text, re.X)
                    if len(text[0]) == 2:
                        money = text[0][0]
                        experience = text[0][1]
                    else:
                        money = " "
                        experience = " "

                except:
                    education = " "
                    money = " "
                    experience = " "

                # 公司名称
                try:
                    company = li.find("div", class_='company_name').find_next("a").text
                except:
                    company = " "

                # 将岗位名称、公司地址、学历要求、薪资、经验要求、公司名称存放到列表中
                infoList.append([name, address, education, money, experience, company])
                a += 1
    except:
        print("招聘信息个数有变化")


# 数据保存
# 数据保存至外部文件excel
def saveData(infoList):
    print("save........")
    workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象
    movieBook = workbook.add_sheet("sheet1")  # 创建工作表
    head = ["岗位名称", "公司地址", "学历要求", "薪资", "经验要求", "公司名称"]
    for i in range(0, len(head)):
        movieBook.write(0, i, head[i])  # 参数1是行，参数2是列，参数3是值

    # 数据逐行输入
    y = 1
    for a in infoList:
        for x in range(0, len(a)):
            movieBook.write(y, x, a[x])
        y += 1
    print("总共保存了" + str(y) + "家招聘信息")
    print("数据保存成功")
    print("数据保存程序执行完毕")

    workbook.save("拉勾网招聘信息3.xls")  # 保存数据表


if __name__ == '__main__':
    getHtml()

