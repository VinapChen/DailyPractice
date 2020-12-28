# coding: utf8
import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        if (count % length != 0):
            add = length - (count % length)
        else:
            add = 0
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')


if __name__ == '__main__':
    key = "557422002DD28BB35888215455FE4156".decode("hex")
    pc = prpcrypt(key)  # 初始化密钥
    hex_string = "ac2a860c99e21549e7f16c2979c13531"
    hex_string1 = "191863e2750932babcb38e190f67fb26"
    hex_string2 = "4766722bdb7f30a0d98a89fc8b1036cf"

    # a = hex_string.decode("hex")

    # e = pc.encrypt(a)
    # print e
    d = pc.decrypt(hex_string)
    d1 = pc.decrypt(hex_string1)
    d2 = pc.decrypt(hex_string2)
    print d.encode('hex')
    print d1.encode('hex')
    print d2.encode('hex')

    # 53 76 2a 3a 38 e3 f0 b2 5b 8a 20 54 6d d9 41 76
    # d = pc.decrypt(hex_string1)
    # print d.encode('hex')
    # e = pc.encrypt("00000000000000000000000000")
    # d = pc.decrypt(e)
    # print e, d.encode('hex')