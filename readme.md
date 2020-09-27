# 框架模型设计
 
```python
    # 用例数据，测试用例、  测试报告、  日志、  配置文件
    # 公共的方法  表格数据读取  数据库校验  
    # 测试运行启动程序  测试套件
```

## 一、 分层设计思想：
- 公共的方法目录：common
- 测试用例类模块目录：testcases
- 测试数据目录：data
- 测试报告存放目录：reports
- 配置文件存放目录：conf
- 日志文件存放的目录：logs
- 项目的启动文件：run_test.py


## 二、数据驱动思想
- 以用例数据来生成测试用例(数据驱动用例生成),有多少条用例数据，生成多少条测试用例。


## 三、程序运行流程思路：
- 1、创建测试套件
- 2、添加测试用例到套件
    - 生成测试用例
        - 读取excle中的测试用例数据
        - 使用ddt根据用例数据来生成测试用例
    - 创建loader对象，将指定路径下的测试用例加载过来 
- 3、执行测试用例程序，生成测试报告
    - runner.run(suiter)
        - 遍历出套件中所有测试用例，一条一条去执行
        - 每一条测试用例执行的流程：
            - 1、获取用例数据
            - 2、发送请求参数到接口地址(单元测试：调用功能函数，传入参数)
            - 3、获取返回的实际结果，和预期结果进行断言，看用例是否执行通过
            
            
