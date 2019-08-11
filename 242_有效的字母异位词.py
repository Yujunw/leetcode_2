'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
'''
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or set(s) != set(t):
            return False
        s_count = Counter(s)
        t_count = Counter(t)

        for char in s:
            if s_count[char] != t_count[char]:
                return False
        return True


S = Solution()
s = "aabbc"
t = "aaabc"
print(S.isAnagram(s, t))
