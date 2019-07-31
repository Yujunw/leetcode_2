'''
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

当 needle 是空字符串时我们应当返回 0 。
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        # if haystack == needle:
        #     return 0

        h, n = len(haystack), len(needle)
        if h < n:
            return -1
        for i in range(h - n + 1):
            j = 0
            if haystack[i] == needle[j]:
                if haystack[i:i + n] == needle:
                    return i
        return -1


s = Solution()

haystack = "pi"
needle = "pi"
print(s.strStr(haystack, needle))
