# -*- coding: utf-8 -*-
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# h 指数的定义: “一位有 h 指数的学者，代表他（她）的 N 篇论文中至多有 h 篇论文，分别被引用了至少 h 次，其余的 N - h 篇论文每篇被引用次数不多于 h 次。”
class Solution(object):
    # 移动0
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i= 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[index-i] = nums[index]
            else:
                i+=1
        for index1 in range(i):
            nums[index1+len(nums)-i] = 0

        print nums
    # h指数
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        for index in range(len(citations)):
            if citations[index] >= (len(citations) - index):
                print (len(citations) - index)
                break

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 1
        countmax = 1
        print nums
        for index in range(len(nums)-1):
            if nums[index] == (nums[index+1]-1):
                count += 1
                print "count:",count
            else:
                if count > countmax:
                    countmax = count
                count = 0

        if len(nums) > 0:
            if count>countmax:
                print countmax
                return countmax
            else:
                print count
                return count
        else:
            print 0
            return 0
arr1 = [0,2,1,-2]
print arr1
s = Solution()
s.longestConsecutive(arr1)

