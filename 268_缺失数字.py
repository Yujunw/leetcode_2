'''
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
求和，然后和1到n项的数列和对比，相差的数就是缺的这个数
'''


class Solution:
    def missingNumber(self, nums):
        length = len(nums)
        x = sum(range(length + 1))
        y = sum(nums)
        return x - y


s = Solution()
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(s.missingNumber(nums))
