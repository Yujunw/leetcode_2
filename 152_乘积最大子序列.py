# -*- coding:utf-8 -*-
# @Time    : 2019/8/14 20:25
# @Author  : Junwu Yu

'''
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

动态规划，最重要的时找到初始状态和状态方程
在此题中，我们用原数组存储子序列乘积
初始状态：nums[0] = nums[0]
状态方程：nums[i] = max(nums[i-1]*nums[i], nums[i])

本题的解题思路是同时记录当前最大值和最小值imax, imin
对于乘法，在遍历数组中，若nums[i]是负数，那么当前最大值imax * nums[i]会变成当前最小值（负数），因此不能简单的只记录最大值。
'''


class Solution:
    def maxProduct(self, nums):
        imax = imin = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            res = max(imax, res)

        return res


s = Solution()
nums = [2, 3, -2, 4]

print(s.maxProduct(nums))
