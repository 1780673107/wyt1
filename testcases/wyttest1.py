import requests

url='http://test.lemonban.com/futureloan/mvc/api/member/login'
params={"mobilephone": "15677889900",'pwd':'123qwe'}
res=requests.post(url=url,params=params)
cookies=res.cookies
print(res.text)

