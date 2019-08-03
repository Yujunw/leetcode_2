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
        def __dfs(combination, strs):
            # t = []
            if combination == reversed(combination):
                res.append(combination)

            for i in range(len(strs)):
                temp_str = strs[0:i]+strs[i+1:-1]
                __dfs(combination+s[i], temp_str)

        res = []

        if s:
            res.append(__dfs('', s))
        return res


s  = Solution()
strs = 'aab'
print(s.partition(strs))
