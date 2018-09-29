# -*- coding:UTF-8 -*-
#字符串操作

class String(object):
    def test(self,str):
        if len(str) == 11 and str[0] == '1' or str[0] == '3':
            str = '0'+str
        return str


s = String()
test_string = '13181401263'

str = s.test(test_string)
print len(str),str