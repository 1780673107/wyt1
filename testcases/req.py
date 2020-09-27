import requests

from common.md5 import Poststr

Poststr
url='http://sandboxapi.kdniao.com:8080/kdniaosandbox/gateway/exterfaceInvoke.json'
EBusinessID='test1672137'
key='d9049b87-3094-4419-b95b-6eecfc1aabc0'

headers={'Content-Type':'application/x-www-form-urlencoded '}
data=Poststr
print(requests.post(url=url,headers=headers,data=data).text)
