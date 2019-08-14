# -*- coding:utf-8 -*-
# @Time    : 2019/8/14 15:44
# @Author  : Junwu Yu

'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:
输入: "race a car"
输出: false
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        s = s.lower()
        res = ''
        for char in s:
            if char.isalnum() or char.isdigit():
                res += char
        return res == ''.join(list(reversed(res)))

    def fun(self, s):
        # 双指针，时间复杂度O(n)
        if not s:
            return True

        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j > -1 and not s[j].isalnum():
                j -= 1

            if i > j:
                return True

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        return True


s = Solution()
strs = '.,'
print(s.fun(strs))
