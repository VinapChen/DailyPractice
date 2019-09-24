# -*- coding: utf-8 -*-
import random
import re
import socket
import struct
import time


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

def send_msg(msg):
    hex_code = "7e"+msg+str(hex(check_crc(msg))).split("0x",1)[1]+"7e"
    string = ''
    tmp1 = re.findall(r'.{2}', hex_code)
    for r in range(len(tmp1)):
        string += struct.pack('B',int(tmp1[r],16))

    my_bytes = bytearray(string)
    print "send package data:",dec2hex4string(my_bytes)
    s.sendall(my_bytes)

def rec_data():
    data = s.recv(1024)
    my_bytes = bytearray(data)
    print "rec package data:", dec2hex4string(my_bytes), "length:", len(data)

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务端
    s.connect(('127.0.0.1', 20048))
    # s.connect(('101.200.89.11', 20048))

    # 请求 | 发送数据到服务端
    # device_id = "022101167123"
    # device_id = raw_input("input the device id:")

    # rand_data = str(hex(random.randint(0,0xff))).split("0x",1)[1]
    # if len(rand_data) < 2:
    #     rand_data = "0"+rand_data
    # package_data = "85aa0000"+device_id+rand_data
    auth_msg = "0102000202210116712300003131"
    package_data = "05000064022101167123000500010000000000000801000000000000000000003531000070010108002430011F310100E10400000000E2020000E306001E0DFB0000E42C01CC0000262300000E251F000000000000000000006300000000000000000000638218200000700000000000"
    # print hex_code

    send_msg(auth_msg)


    # 响应 | 接受服务端返回到数据
    while(1):
        rec_data()
        time.sleep(3)

    # 关闭 socket
    # s.close()


    # hex_code = '7e0102000202210116712300003131677e'
    # hex_code = '7e85aa000002210116712300125b7e'
    # hex_code = "7e00020000022101167123003e5a7e"