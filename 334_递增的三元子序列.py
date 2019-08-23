# -*- coding:utf-8 -*-
# @Time    : 2019/8/23 18:55
# @Author  : Junwu Yu

'''
给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:

输入: [1,2,3,4,5]
输出: true
示例 2:

输入: [5,4,3,2,1]
输出: false
'''


class Solution:
    def increasingTriplet(self, nums) -> bool:
        '''
        min_num始终记录最小元素，max_num为某个子序列里第二大的数。
        接下来不断更新 min_num，同时保持 max_num尽可能的小。
        如果下一个元素比 b 大，说明找到了三元组。
        '''
        if len(nums) < 3:
            return False

        min_num = float('inf')
        max_num = float('inf')

        for num in nums:
            if num < min_num:
                min_num = num
            elif min_num < num <= max_num:
                max_num = num
            elif num > max_num:
                return True
        return False
