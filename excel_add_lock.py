# -*- coding: utf-8 -*-
import requests
import xlrd
import json,urllib2
import operator
import os


if __name__ == '__main__':
    # 打开excel文件
    data1 = xlrd.open_workbook("file")
    # 读取第一个工作表
    table = data1.sheets()[0]
    # 统计行数
    n_rows = table.nrows

    for v in range(1, n_rows-1):
        values = table.row_values(v)[0]
        print values,type(values),len(values),values[-10:]
        # data='{"appkey":"56a0a88c4407a3cd028ac2fe","bike_number":"%s", "aes_key":"11111111000000000000000011111111", "ble_mac_addr":"00:11:22:33:44:55", "imei":"%s", "lock_type":3}'%(values[-10:],values)
        # print data
        # requrl = "http://abj-elogic-test1.yunba.io:39788/add"

        command = 'curl -H "Content-type: application/json; charset=utf-8" \
    -XPOST\
    -d \'{"appkey":"56a0a88c4407a3cd028ac2fe","bike_number":"%s", "aes_key":"11111111000000000000000011111111", "ble_mac_addr":"00:11:22:33:44:55", "imei":"%s", "lock_type":3}\'\
    http://abj-elogic-test1.yunba.io:39788/add'%(values[-10:],values)
        print command
        print os.system(command)


