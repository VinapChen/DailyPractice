# -*- coding: utf-8 -*-
import socket
import ssl


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



class client_ssl:



    def send_hello(self,):
        client1 = client_ssl()
        # 生成SSL上下文
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        # 加载信任根证书
        context.load_verify_locations("/Users/yunba/Downloads/client.p12")

        #与服务端建立socket连接
        with socket.create_connection(('182.92.1.50', 8898)) as sock:
            # 将socket打包成SSL socket
            # 一定要注意的是这里的server_hostname不是指服务端IP，而是指服务端证书中设置的CN
            with context.wrap_socket(sock, server_hostname='182.92.1.50') as ssock:
                msg = "CS*865339003627912*0003*CON".encode("utf-8")
                msg_lk = "CS*0009*LK,0,0,83".encode("utf-8")
                msg_ud = "CS*0009*LK,0,0,83".encode("utf-8")
                msg_ud2 = "CS*00BD*UD2,120118,070625,A,22.570720,N,113.8620167,E,0.00,188.6,0.0,9,100,51,14188,0,00000010,6,255,460,0,9360,5081,156,9360,4081,129,9360,4151,128,9360,5082,127,9360,4723,122,9360,4082,120,0,22.4".encode(
                    "utf-8")
                msg_al = "CS*00BC*AL,120118,070625,A,22.570720,N,113.8620167,E,0.00,188.6,0.0,9,100,51,14188,0,00010008,6,255,460,0,9360,5081,156,9360,4081,129,9360,4151,128,9360,5082,127,9360,4723,122,9360,4082,120,0,22.4".encode(
                    "utf-8")

                while 1:
                    com = input()

                    if ("con" == com):
                        ssock.send(msg)
                        print("send:", msg)
                        # 接收服务端返回的信息
                        msg_rec = ssock.recv(128)
                        # my_bytes = bytearray(msg)
                        print("rec:", str(msg_rec, encoding="utf-8"))

                    elif ("exit" == com):
                        ssock.close()
                        break
                    elif ("lk" == com):
                        ssock.send(msg_lk)
                        print("send:", msg_lk)
                        # 接收服务端返回的信息
                        msg_rec = ssock.recv(128)
                        print("rec:", str(msg_rec, encoding="utf-8"))

                        msg_rec = ssock.recv(128)
                        print("rec:", str(msg_rec, encoding="utf-8"))

                    elif ("ud2" == com):
                        ssock.send(msg_ud2)
                        # 无回复
                        # msg_rec = ssock.recv(128)
                        print("send:", msg_ud2)
                        # print("rec:", str(msg_rec, encoding = "utf-8"))
                    elif ("al" == com):
                        ssock.send(msg_al)
                        print("send:", msg_al)
                        # 接收服务端返回的信息
                        msg_rec = ssock.recv(128)
                        print("rec:", str(msg_rec, encoding="utf-8"))


if __name__ == "__main__":
    client = client_ssl()
    client.send_hello()
