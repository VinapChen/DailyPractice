# -*- coding: utf-8 -*-
import requests
import xlrd
import json,urllib2
import operator
import os


if __name__ == '__main__':
    # 打开excel文件
    data1 = xlrd.open_workbook("/Users/yunba/Downloads/SN号-150把.xlsx")
    # 读取第一个工作表
    table = data1.sheets()[0]
    # 统计行数
    n_rows = table.nrows
    print n_rows
    for v in range(12, n_rows):
        imei = table.row_values(v)[1]
        # print imei,len(imei)
        aes_key = table.row_values(v)[2]
        # print aes_key,len(aes_key)

        sn = imei[2:]
        mac = imei[0:2] + ":" + imei[2:4] + ":" + imei[4:6] + ":" + imei[6:8] +":"+ imei[8:10] + ":" + imei[10:12]
        print sn,imei,mac,aes_key
        # data='{"appkey":"56a0a88c4407a3cd028ac2fe","bike_number":"%s", "aes_key":"11111111000000000000000011111111", "ble_mac_addr":"00:11:22:33:44:55", "imei":"%s", "lock_type":3}'%(values[-10:],values)
        # print data
        # requrl = "http://abj-elogic-test1.yunba.io:39788/add"

        command = 'curl -H "Content-type: application/json; charset=utf-8" \
    -XPOST\
    -d \'{"appkey":"56a0a88c4407a3cd028ac2fe","bike_number":"%s", "aes_key":"%s","password": "303030303030", "ble_mac_addr":"%s", "imei":"%s", "lock_type":6}\'\
    http://abj-elogic-test1.yunba.io:39788/add'%(sn,aes_key,mac,imei)
        print command
        print os.system(command)


