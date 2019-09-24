# -*- coding: utf-8 -*-
import random
import re
import socket
import struct
import binascii
import time
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/scooter', methods=['GET'])
def index():

    imei = request.args.get("imei")
    operate = request.args.get("operate")
    print imei,operate
    scooter_go_client(imei,operate)

    resp = make_response("success")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


def scooter_go_client(imei,operate):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务端
    s.connect(('127.0.0.1', 8082))


    # 请求 | 发送数据到服务端
    msg_q = "*SCOR,OM,%s,Q0,414,99,31#\n" % imei
    msg_r = "*SCOS,OM,123456789123456,R0,0,20,1234,1566200630#\n"
    msg_l = "*SCOS,OM,123456789123456,L0,55,1234,1566200630#\n"
    msg_d = "*SCOR,OM,%s,D0,0,072417.089,V,,,,,0,,070180,,M,N#\n" % imei

    # 867584031521425
    msg_unlock = "unlock,%s,\n" % imei
    msg_lock = "lock,%s,\n" % imei
    # command = raw_input()

    if operate == "register":
        b = binascii.b2a_hex(msg_q)
    elif operate == "unlock":
        b = binascii.b2a_hex(msg_unlock)
    elif operate == "lock":
        b = binascii.b2a_hex(msg_lock)

    # print b
    string = ''
    tmp1 = re.findall(r'.{2}', b)
    for r in range(len(tmp1)):
        string += struct.pack('B', int(tmp1[r], 16))

    s.sendall(string)

    # 响应 | 接受服务端返回到数据
    # data = s.recv(1024)
    # print data
    # time.sleep(3)

    # 关闭 socket
    s.close()


if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 5000,
        debug = True )