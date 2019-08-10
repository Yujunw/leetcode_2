'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:
输入: nums = [1], k = 1
输出: [1]
说明：
你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
'''

import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 0

        l = sorted(d.items(), key=lambda x: x[1], reverse=True)
        res = [key for key, val in l]
        return res[:k]

    def fun(self, nums, k):
        '''
        建堆
        Counter（计数器）：用于追踪值的出现次数
        Counter类继承dict类，所以它能使用dict类里面的方法
        :param nums:
        :param k:
        :return:
        '''
        # 时间复杂度O(n)
        count = Counter(nums)
        # 建堆和输出的复杂度是 O(Nlog(k))
        return heapq.nlargest(k, count.keys(), key=count.get)


s = Solution()
nums = [1, 1, 1, 2, 2, 2, 3]
k = 2
print(s.fun(nums, k))
