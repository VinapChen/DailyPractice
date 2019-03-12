# -*- coding: utf-8 -*-

import requests
import json,urllib2

# data = {"data":{"title":"John P Rees","subTitle":"Senior Director of Operations"},"temp_id":1,"size":1}
# data = {"data":{"title":"云巴智能价签",
#                 "subTitle1":"低功耗",
#                 "subTitle2":"深圳南山",
#                 "currency":"¥",
#                 "price":'12.255',
#                 "productNumber":'6925785604585'},"temp_id":0,"size":0}
data = {
      	# "saa":"true",

        "data":{
                "v":"6.1.0",
                "u":1,
                # "ss":"1440x2560",
                "mcc":1,
                # "t":1,
                "lan":1,
                "ch":1,
                "bi":1,
                # "sign":"2298FAF0E575556CFCD7037D8B6C3630",
                "f":1,
                "ui":101,
        }
      }

# payload = {"sales":[{"name":2008,"Clothes":300,"Food":235,"Electronics":304},{"name":2009,"Clothes":384,"Food":258,"Electronics":411},{"name":2010,"Clothes":342,"Food":381,"Electronics":319},{"name":2011,"Clothes":468,"Food":241,"Electronics":402},{"name":2012,"Clothes":232,"Food":185,"Electronics":546},{"name":2013,"Clothes":245,"Food":184,"Electronics":454},{"name":2014,"Clothes":404,"Food":206,"Electronics":354},{"name":2015,"Clothes":244,"Food":188,"Electronics":301}]}
# requrl = "http://abj-pubackstat-1.yunba.io:8080/txt2json"
# requrl = "http://0.0.0.0:8081/lockimage/getInfoStream.do"
requrl = "http://0.0.0.0:8082/lockimage/logUpload.do?v=6.1.1&f=1&mcc=1&lan=1&ch=1&bi=1"
# requrl = "http://abj-elogic-test1.yunba.io:9970/lock"

# headers = {'Content-Type': 'application/json'}    ## headers中添加上content-type这个参数，指定为json格式
# response = requests.post(url=requrl, headers=headers, data=json.dumps(data))    ## post的时候，将data字典形式的参数用json包转换成json格式。
# res= response.read()

# print  res

req = urllib2.Request(requrl)

req.add_header('Content-Type', 'application/json')
req.add_header('encoding', 'utf-8')
req.add_header('User-Agent',' - - - - - /test')
req.add_header('X-Forwarded-For','127.0.0.1,')
# response = urllib2.urlopen(req)

response = urllib2.urlopen(req, json.dumps(data,ensure_ascii=False))
result = response.read()
print(result)



# req = urllib2.Request(url, data)
# result = urllib2.urlopen(req)

# r = requests.get(requrl,params = payload)

# print (result)
# res = json.loads(result)
#
# print (type(res))
# msg= res["ResultMsg"]
# print ms["value"]
