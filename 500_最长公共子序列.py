# -*- coding:utf-8 -*-
# @Time    : 2019/8/29 15:16
# @Author  : Junwu Yu

'''
求两个字符串的 LCS 长度：

输入: str1 = "abcde", str2 = "ace"
输出: 3
解释: 最长公共子序列是 "ace"，它的长度是 3

二维动态规划
'''


class Solution:
    def longestCommonStrings(self, s1, s2):
        m, n = len(s1), len(s2)
        # 定义二维数组，(m+1)*(n+1),dp[i][j]代表s1[:i]与s2[:j]的LCS
        # 初始状态，第0行第0列均为0，其他位置默认为0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
