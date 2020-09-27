''''''

import base64
import hashlib
import os
from urllib import parse

from common.constant import DATA_DIR
from common.read_excel import ReadExcel


def md5(data):
    return (hashlib.md5(data.encode(encoding='UTF-8')).hexdigest())
    #md5加密，这里的data要传字符串

def base(data):

    return str(base64.b64encode(data.encode("utf-8")), "utf-8")
    # base64加密，这里的data要传字符串
def url1(data):
    return parse.quote(data)
    #url编码

data_file_path = os.path.join(DATA_DIR, "cases.xlsx")

id='test1672137'
RequestType=1002
keyValue="d9049b87-3094-4419-b95b-6eecfc1aabc0"
url= "https://api.kdniao.com/Ebusiness/EbusinessOrderHandle.aspx"
DataType = "2"
jsonStr = "{\"OrderCode\":\"\",\"ShipperCode\":\"SF\",\"LogisticCode\":\"118461988807\"}"
RequestData=url1(jsonStr)
datasign=url1(base((md5((jsonStr + keyValue)))))
Poststr='RequestType='+'{}'.format(RequestType)+'&EBusinessID=''{}'.format(id)+'&RequestData=''{}'.format(RequestData)+'&DataSign='+'{}'.format(datasign)+'&DataType=2'


print(Poststr)


