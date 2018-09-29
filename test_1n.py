# -*- coding: utf-8 -*-
# 一副从1到n的牌，每次从牌堆顶取一张放桌子上，再取一张放牌堆底，直到手机没牌，最后桌子上的牌是从1到n有序，设计程序，输入n，输出牌堆的顺序数组
#
# “取一个1～n的数组，这里为了说明取n=5。按照题目中的规则变换，得到数组：[1 3 5 4 2]，将该数组下标与值互换得到[1 5 2 4 3]，即为答案。解释：[1 3 5 4 2]的意义是，经过变换，原数组中3号位置的数字现在2号槽，原数组中5号位置的数字现在3号槽... 现在已知变换后的槽存放的是1～n，故只需将下标与值互换即可得到待求数组。
#
# 这道题还可以继续扩展：
#
# 1.变换规则更复杂使得无法逆向模拟还原原数组；
#
# 2.最终得到的序列可以扩展为任意序列。
n = input('input the numble n: ')

arr = []
arr1 = []
arr2 = []
for index in range(n):
    arr.append(index+1)
    arr1.append(index+1)
    arr2.append(index+1)
print arr


i = 0
for index1 in range(n):
    if (index1%2 == 0):
        arr1[i] = arr[index1]
    else:
        arr1[n-i-1] = arr[index1]
        i = i+1
print arr1

j = 0
for index2 in range(n):
    arr2[arr1[index2]-1] = index2+1;

print arr2

