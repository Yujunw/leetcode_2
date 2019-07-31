'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
所有输入均为小写字母。
不考虑答案输出的顺序。

哈希
'''


class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return []
        d = {}
        for str in strs:
            keys = ''.join(sorted(str))
            if keys in d.keys():
                d[keys].append(str)
            else:
                d[keys] = [str]
        return list(d.values())


s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))
