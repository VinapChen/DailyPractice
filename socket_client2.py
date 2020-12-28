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
    # s.connect(('127.0.0.1', 8899))
    s.connect(('182.92.1.50', 8899))
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
    tmp1 = re.findall(r'.{2}', "0003")
    for r in range(len(tmp1)):
        string += struct.pack('B',int(tmp1[r],16))

    string2 = ''
    tmp2 = re.findall(r'.{2}', "11223344")
    for r in range(len(tmp2)):
        string2 += struct.pack('B', int(tmp2[r], 16))

    print(string)
    string1 = "CfS*01020304052*0003*CON"
    print (string1)

    my_bytes = bytearray(string1)
    print ("package data:",dec2hex4string(my_bytes))

    s.sendall(my_bytes)
    # 响应 | 接受服务端返回到数据
    cer = []
    while 1:
        data = s.recv(4096)
        my_bytes = bytearray(data)
        print(len(data),dec2hex4string(my_bytes))
        part = 1;
        if(len(my_bytes) > 1833):

            cer = my_bytes[24:]
            print (len(my_bytes[24:]),dec2hex4string(my_bytes[24:]))
            f = open('/Users/yunba/Downloads/output.p12', 'wb')
            f.write(cer)
            f.close()
        elif (part == 1):
            cer = my_bytes[24:]
            part = 2
        elif (part == 2):
            cer = cer + my_bytes
            print (len(cer), dec2hex4string(cer))
            f = open('/Users/yunba/Downloads/output.p12', 'wb')
            f.write(cer)
            f.close()
            part = 1



    # 关闭 socket
    s.close()


