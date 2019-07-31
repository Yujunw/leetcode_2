'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:
输入: dividend = 10, divisor = 3
输出: 3
示例 2:
输入: dividend = 7, divisor = -3
输出: -2

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

计算机中的移位运算是乘（左移）除（右移）2
'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # ^ 按位异或运算符：当两对应的二进位相异时，结果为1，两个True或者False异或得到0，一个True和False异或得到1
        sign = (dividend > 0) ^ (divisor > 0)

        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend >= divisor:
            # divisor向左移动一位，相当于乘以2，直到它大与被除数
            divisor = divisor << 1
            count += 1
        result = 0
        while count > 0:
            count -= 1
            divisor = divisor >> 1


s = Solution()
dividend = 10
divisor = 3
print(s.divide(dividend, divisor))
