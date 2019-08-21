'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

解决这类 “最优子结构” 问题，可以考虑使用 “动态规划”：

1、定义 “状态”；
2、找到 “状态转移方程”。
初始状态是什么？状态转移方程是什么？
https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        max_len = s[0]
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if (s[i] == s[j]) & (self.is_Palindrome(s[i:j+1])):
                    if len(s[i:j+1]) > len(max_len):
                        max_len = s[i:j+1]
        return max_len

    def is_Palindrome(self, s):
        # flag = True
        if len(s) <= 1:
            return False
        l = list(s)
        while len(l) > 1:
            if l.pop(0) != l.pop(-1):
                return False

        return True

    # 动态规划
    def dp(self, s):

        if not s:
            return ''
        size = len(s)

        dp = [[False for _ in range(size)] for _ in range(size)]
        longest = 1
        res = s[0]

        for r in range(1, size):
            for l in range(r):
                # (r-l <=2)，说明r与l之间最多只有一个数字， 确保去除两端的回味字符之后，只有一个字符这种情况成立
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest:
                        longest = cur_len
                        res = s[l:r + 1]

        return res

s = Solution()
s1 = 'ccc'
# print(s1[2:4])
# print(s.is_Palindrome(s1))
print(s.dp(s1))

