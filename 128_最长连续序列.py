# -*- coding:utf-8 -*-
# @Time    : 2019/8/22 13:18
# @Author  : Junwu Yu

'''
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。
示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''


class Solution:
    def longestConsecutive(self, nums) -> int:
        # 位图法，memorry error
        if len(nums) == 0:
            return 0
        l = [-1] * (max(nums) + 1)
        max_count = 0
        temp_count = 0
        for i in range(len(nums)):
            l[nums[i]] = nums[i]

        for j in range(len(l)):

            if l[j] == j:
                temp_count += 1
            else:
                temp_count = 0

            if temp_count > max_count:
                max_count = temp_count

        return max_count

    def longestConsecutive_2(self, nums) -> int:
        # 哈希法
        # 用dict记录当前值所在子序列的长度
        hash_dict = dict()
        max_length = 0

        for num in nums:
            if num not in hash_dict:
                # dict.get() 如果指定键的值不存在时，返回该默认值
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)
                curr_length = 1 + left + right

                if curr_length > max_length:
                    max_length = curr_length

                # num， num-left， num+right 在同一个序列，所以它们的值相同
                hash_dict[num] = curr_length
                hash_dict[num - left] = curr_length
                hash_dict[num + right] = curr_length

        return max_length


s = Solution()
nums = [100, 4, 200, 1, 3, 2, 101, 99, 97, 96, 98]
print(s.longestConsecutive_2(nums))
