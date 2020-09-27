import requests

from common.md5 import Poststr






url='http://sandboxapi.kdniao.com:8080/kdniaosandbox/gateway/exterfaceInvoke.json'
headers={'Content-Type':'application/x-www-form-urlencoded '}


res=requests.post(url=url,headers=headers,data=Poststr)
