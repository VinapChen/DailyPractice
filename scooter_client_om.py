# -*- coding: utf-8 -*-
import binascii
import random
import re
import socket
import struct
import thread
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
            temp_item = "0" + temp_item
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
    hex_code = "7e" + msg + str(hex(check_crc(msg))).split("0x", 1)[1] + "7e"
    string = ''
    tmp1 = re.findall(r'.{2}', hex_code)
    for r in range(len(tmp1)):
        string += struct.pack('B', int(tmp1[r], 16))

    my_bytes = bytearray(string)
    print "send package data:", dec2hex4string(my_bytes)
    s.sendall(my_bytes)


def rec_data():
    while (1):
        data = s.recv(1024)
        my_bytes = bytearray(data)
        print "rec package data:", dec2hex4string(my_bytes), "length:", len(data)
        print data
        if len(data) == 0:
            s.close()
        deal_data(data)
        time.sleep(3)

def deal_data(data):
    data_arr = str.split(data[2:], ",")
    if data_arr[0] == "*SCOS" and data_arr[1] == "OM" and len(data_arr) > 4:
        imei = data_arr[2]
        oper = data_arr[4]
        if data_arr[3] == "R0":
            resp = "*SCOR,OM," + imei + ",R0," + oper +",254,0," + str(int(time.time())) +"#\n"
            b = binascii.b2a_hex(resp)
            string = ''
            tmp1 = re.findall(r'.{2}', b)
            for r in range(len(tmp1)):
                string += struct.pack('B', int(tmp1[r], 16))
            s.sendall(string)
        elif data_arr[3] == "L0":
            resp = "*SCOR,OM," + imei + ",L0,0,0," + str(int(time.time())) + "#\n"
            b = binascii.b2a_hex(resp)
            string = ''
            tmp1 = re.findall(r'.{2}', b)
            for r in range(len(tmp1)):
                string += struct.pack('B', int(tmp1[r], 16))
            s.sendall(string)
        elif data_arr[3] == "L1":
            resp = "*SCOR,OM," + imei + ",L1,0,0," + str(int(time.time())) + "#\n"
            b = binascii.b2a_hex(resp)
            string = ''
            tmp1 = re.findall(r'.{2}', b)
            for r in range(len(tmp1)):
                string += struct.pack('B', int(tmp1[r], 16))
            s.sendall(string)

def send_package(command):

    auth_msg = "0102000202210116712300003131"
    auth_msg1 = "0102000202210116712400003131"

    control_resp = "05000064022101167123000500010000000000000801000000000000000000003531000070010108002430011F310100E10400000000E2020003E306001E0DFB0000E42C01CC0000262300000E251F000000000000000000006300000000000000000000638218200000700000000000"
    device_info_unlock = "0200006202210116712300050000000000000001000000000000000000000000000070010108003030011F310100E10400000001E2020003E306001D0DD70000E42C01CC0000262300000E251F000000000000000000006300000000000000000000630000000000000000000000"
    device_info_lock = "02000062022101167123018b0000000000000801000000000000000000000000000019080216464430011f310100e10400000004e2020004e306001e0e070000e42c01cc0000262300000e251f01cc00009763000048521301cc00009763000038521608130c022f340000000101"
    heart_beat = "000200000221011671230004"


    imei = "867584031521425"
    msg_q = "*SCOR,OM,%s,Q0,414,99,31#\n" % imei
    msg_r = "*SCOS,OM,123456789123456,R0,0,20,1234,1566200630#\n"
    msg_l = "*SCOS,OM,123456789123456,L0,55,1234,1566200630#\n"
    msg_d = "*SCOR,OM,%s,D0,0,072417.089,V,,,,,0,,070180,,M,N#\n" % imei
    msg_hb = "*SCOR,OM,%s,H0,1,410,31,90,0#\n" % imei
    msg_d = "*SCOR,OM,%s,D0,0,091125.000,A,2232.65730,N,11356.06394,E,3,6.47,,42.17,M,A#\n" %imei

    # 867584031521425
    msg_unlock = "unlock,%s,\n" % imei
    msg_lock = "lock,%s,\n" % imei
    #
    # if command == "auth":
    #     send_msg(msg_q)
    # elif command == "auth1":
    #     send_msg(auth_msg1)
    # elif command == "ctrl_resp":
    #     send_msg(control_resp)
    # elif command == "info_lock":
    #     send_msg(device_info_lock)
    # elif command == "info_unlock":
    #     send_msg(msg_unlock)
    # elif command == "hb":
    #     send_msg(heart_beat)

    if command == "register":
        b = binascii.b2a_hex(msg_q)

        string = ''
        tmp1 = re.findall(r'.{2}', b)
        for r in range(len(tmp1)):
            string += struct.pack('B', int(tmp1[r], 16))

        s.sendall(string)

    elif command == "unlock":
        b = binascii.b2a_hex(msg_unlock)
        string = ''
        tmp1 = re.findall(r'.{2}', b)
        for r in range(len(tmp1)):
            string += struct.pack('B', int(tmp1[r], 16))

        s.sendall(string)
    elif command == "msg_hb":
        b = binascii.b2a_hex(msg_hb)
        string = ''
        tmp1 = re.findall(r'.{2}', b)
        for r in range(len(tmp1)):
            string += struct.pack('B', int(tmp1[r], 16))

        s.sendall(string)
    elif command == "msg_d":
        b = binascii.b2a_hex(msg_d)
        string = ''
        tmp1 = re.findall(r'.{2}', b)
        for r in range(len(tmp1)):
            string += struct.pack('B', int(tmp1[r], 16))

        s.sendall(string)
    elif command == "lock":
        b = binascii.b2a_hex(msg_lock)
        string = ''
        tmp1 = re.findall(r'.{2}', b)
        for r in range(len(tmp1)):
            string += struct.pack('B', int(tmp1[r], 16))

        s.sendall(string)


def input_command():
    while 1:
        command = raw_input()
        send_package(command)


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务端
    # s.connect(('127.0.0.1', 8082))
    # s.connect(('101.200.89.11', 20048))

    # 请求 | 发送数据到服务端
    # device_id = "022101167123"
    # device_id = raw_input("input the device id:")

    # rand_data = str(hex(random.randint(0,0xff))).split("0x",1)[1]
    # if len(rand_data) < 2:
    #     rand_data = "0"+rand_data
    # package_data = "85aa0000"+device_id+rand_data
    # print hex_code

    # send_msg(auth_msg)

    try:
        thread.start_new_thread(rec_data, ())
        thread.start_new_thread(input_command, ())
    except:
        print "Error: unable to start thread"

    while 1:
        pass
    # 关闭 socket
    # s.close()

    # hex_code = '7e0102000202210116712300003131677e'
    # hex_code = '7e85aa000002210116712300125b7e'
    # hex_code = "7e00020000022101167123003e5a7e"