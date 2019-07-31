'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

子列表中的第一个元素是否小于前一个子列表的第二个元素，是的话就将两个列表合并，是否小于前一个子列表的第以个元素，是的话就直接删除前一个列表
'''


class Solution:

    # def merge(self, intervals):
    #
    #     if len(intervals) == 0 or len(intervals) == 1:
    #         return intervals
    #     res = []
    #     for i in range(1,len(intervals)):
    #         if intervals[i][0] <= intervals[i-1][1]:
    #             if intervals[i][0] < intervals[i-1][0]:
    #                 res.append(intervals[i])
    #             else:
    #                 res.append([intervals[i-1][0],intervals[i][1]])
    #         else:
    #             res.append(intervals[i])
    #
    #     return res
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            # 如果res为空或者res最后一个子列表的最后一个元素小于interval[0]
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            if interval[0] <= res[-1][1]:
                if interval[1] > res[-1][1]:
                    res[-1][1] = interval[1]

        return res


s = Solution()
intervals = [[1, 3]]
print(s.merge(intervals))
