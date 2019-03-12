# 给定一个 24 小时制（小时:分钟）的时间列表，找出列表中任意两个时间的最小时间差并已分钟数表示。
#
#
# 示例 1：
#
# 输入: ["23:59","00:00"]
# 输出: 1
#
# 备注:
#
# 列表中时间数在 2~20000 之间。
# 每个时间取值在 00:00~23:59 之间。
import time

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # timePoints.sort()
        # # print(timePoints)
        # diff = 1440
        # for i in range(len(timePoints)):
        #     if i > 0:
        #         h2 = (int(timePoints[i][0])*10 + int(timePoints[i][1]))*60\
        #             +int(timePoints[i][3])*10 + int(timePoints[i][4])
        #
        #         h1 = (int(timePoints[i-1][0]) * 10 + int(timePoints[i-1][1]))*60\
        #             +int(timePoints[i-1][3]) * 10 + int(timePoints[i-1][4])
        #         if ( h2- h1) < diff :
        #             diff = h2 - h1
        # h1 = (int(timePoints[0][0]) * 10 + int(timePoints[0][1]))*60\
        #     +int(timePoints[0][3]) * 10 + int(timePoints[0][4])
        #
        # h2 = (int(timePoints[len(timePoints) - 1][0]) * 10 + int(timePoints[len(timePoints) - 1][1]))*60\
        #     +int(timePoints[len(timePoints) - 1][3]) * 10 + int(timePoints[len(timePoints) - 1][4])
        # return min(diff,(1440-h2+h1))

        diff = [0] * 1440
        for time in timePoints:
            num = (int(time[0])*10 + int(time[1]))*60 + int(time[3])*10 + int(time[4])
            if diff[num]:
                return 0
            else:
                diff[num] = 1

        last = 0
        mindiff = 1400

        for i in range(1440):
            if diff[i]:
                first = i
                break
        last = first
        for i in range(first+1,1440):
            if diff[i]:
                nowdiff = i - last

                if nowdiff < mindiff:
                    mindiff = nowdiff

                last = i

        return min(mindiff,(1440 - last + first))



if __name__ == '__main__':
    s = Solution()
    timePoints = ["23:59","00:00"]
    print(s.findMinDifference(timePoints))
