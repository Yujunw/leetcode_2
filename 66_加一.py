'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [9,9,9]
输出: [1,0,0,0]
解释: 输入数组表示数字 999
'''

class Solution:
    def plusOne(self, digits):
        if not digits:
            return []
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + c
            c = digits[i] // 10
            digits[i] = digits[i] % 10

        if c:
            digits.insert(0, c)
        return digits

s = Solution()
digits = [0]
print(s.plusOne(digits))
# s.plusOne(digits)
