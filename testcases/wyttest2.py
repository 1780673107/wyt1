from testcases.wyttest1 import cookies
import requests

url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
params={"mobilephone":"15677889900","amount":None}
res=requests.post(url=url,params=params,cookies=cookies)
print(res.text)