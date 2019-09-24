# -*- coding: utf-8 -*-
import random
import re
import socket
import struct


def dec2hex4string(val):
    """
    :param val: a tuple ,which include decimal number!
    :return: a tuple ,which include hex number!
    """
    temp = []
    for item in val:
        temp_item = hex(item).replace('0x', '')
        if len(temp_item) < 2:
            temp_item = "0"+temp_item
        # print item,temp_item
        temp.append(temp_item)

    result = ''.join(temp)
    return result


def check_crc(data):
    tmp = re.findall(r'.{2}', data)
    crc = 0x00
    for r in range(len(tmp)):
        crc = crc ^ int(tmp[r], 16)
    return crc


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务端
    s.connect(('127.0.0.1', 1884))
    # s.connect(('101.200.89.11', 1884))

    # 请求 | 发送数据到服务端
    device_id = "022101167123"
    # device_id = raw_input("input the device id:")

    rand_data = str(hex(random.randint(0,0xff))).split("0x",1)[1]
    if len(rand_data) < 2:
        rand_data = "0"+rand_data
    package_data = "85aa0000"+device_id+rand_data

    hex_code = "7e"+package_data+str(hex(check_crc(package_data))).split("0x",1)[1]+"7e"
    # print hex_code

    string = ''
    tmp1 = re.findall(r'.{2}', hex_code)
    for r in range(len(tmp1)):
        string += struct.pack('B',int(tmp1[r],16))

    my_bytes = bytearray(string)
    print "package data:",dec2hex4string(my_bytes)

    s.sendall(string)
    # 响应 | 接受服务端返回到数据
#     data = s.recv(1024)
#     my_bytes = bytearray(data)
#     print(len(data),dec2hex4string(my_bytes))

    # 关闭 socket
    s.close()
