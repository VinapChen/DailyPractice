# -*- coding: utf-8 -*-

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
mark = 0
while(mark==0):
    m = input("input the month:")
    if m<1 or m>12:
        print 'please input true month !'
    else:
        mark =1
mark = 0
while(mark == 0):
    d = input("input the day:")
    if d<1 or d>31:
        print 'please input true day !'
    else:
        mark =1

index_m = (m-1)%3

str = str+str[0:index_m*9]
# print len(str)
str = str[index_m*9:index_m*9+27]
# print str,len(str)
str1 = str[0:9]
str2 = str[9:18]
str3 = str[18:27]

# print str1, str2, str3,len(str1)

index_d = (d-1)%9
str1 = str1+str1[0:index_d]
str1 = str1[index_d:index_d+9]
str2 = str2+str2[0:index_d]
str2 = str2[index_d:index_d+9]
str3 = str3+str3[0:index_d]
str3 = str3[index_d:index_d+9]
str = [str1,str2,str3]
print str1, str2, str3

text = raw_input("input the msg:")
for index in range(0,len(text)):
    for i in range(0,3):
        for j in range(0,9):
            # print i,j,text[index],str[i][j]
            if text[index] == str[i][j]:
                print (i+1)*10+j+1,
                break
# print text,len(text)



