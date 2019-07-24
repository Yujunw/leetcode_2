'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:所有输入只包含小写字母 a-z 。
'''


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        res = ''

        while strs:
            try:
                word = set(map(lambda x: x[0], strs))
                # print(word)
                if len(word) == 1:
                    res += list(word)[0]
                else:
                    return res
                # print(res)
                strs = list(map(lambda x: x[1:],strs))
                # print(strs)
            except:
                # print('error')
                return res
        return res

s = Solution()
strs = ["abc","abcc","abc","abca","abca"]

print(s.longestCommonPrefix(strs))


