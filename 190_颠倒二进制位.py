# -*- coding:utf-8 -*-
# @Time    : 2019/8/15 16:07
# @Author  : Junwu Yu

'''
颠倒给定的 32 位无符号整数的二进制位。
示例 1：

输入: 00000010100101000001111010011100
输出: 00111001011110000010100101000000
解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
      因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
'''


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
        res = 0
        count = 32
        while count:
            # res左移，腾出位置存储n&1
            res <<= 1
            # n & 1，n的最后一位与1相同则n & 1为1，否则为0，因此可以判断n的最后一位
            res += n & 1
            n >>= 1
            count -= 1
        # base=2, 输出为二进制
        return int(bin(res), base=2)


s = Solution()
print(s.reverseBits(0b00000010100101000001111010011100))
