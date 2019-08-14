'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

'''

class Solution:
    def partition(self, s):
        def dfs(combination, strs):
            # t = []
            if combination == combination[::-1] and len(combination) >= 1:
                res.append(combination)

            for i in range(len(strs)):
                temp_str = strs[:i] + strs[i + 1:]
                dfs(combination + strs[i], temp_str)

        res = []
        if s:
            dfs('', s)
        return res


s = Solution()
strs = 'aab'
print(s.partition(strs))
print(strs[:0] + strs[1:])
