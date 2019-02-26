# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
#
# 示例:
#
# 输入: [5,2,6,1]
# 输出: [2,1,1,0]
# 解释:
# 5 的右侧有 2 个更小的元素 (2 和 1).
# 2 的右侧仅有 1 个更小的元素 (1).
# 6 的右侧有 1 个更小的元素 (1).
# 1 的右侧有 0 个更小的元素.

import bisect

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # counts[len(nums)]
        ans = []
        tmp = []
        for i in reversed(nums):
            pos = bisect.bisect_left(tmp, i)
            # 往有序数组tmp里插入i（左侧插入），返回index
            ans.append(pos)
            tmp.insert(pos, i)
        return list(reversed(ans))

if __name__ == '__main__':
    nums = [5,2,6,1]
    s = Solution()
    counters = s.countSmaller(nums)
    print(counters)
