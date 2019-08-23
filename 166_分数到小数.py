# -*- coding:utf-8 -*-
# @Time    : 2019/8/22 10:06
# @Author  : Junwu Yu

'''
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"
'''


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        '''
        无限不循环小数不能表示成两个整数之比
        '''
        x = str(numerator / denominator)
        l = x.split('.')
        # res =


print(1 / 19)
