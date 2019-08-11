'''
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # m=1，则n<3时，直接return False
        while n >= 3:
            n = n / 3

        if n == 1:
            return True
        else:
            return False


s = Solution()
print(s.isPowerOfThree(82))
