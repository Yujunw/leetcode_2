'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
要生成各种排列的问题，就使用回溯算法，DFS+剪枝
'''

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        d = {'2':['a','b','c'],
             '3':['d','e','f'],
             '4':['g','h','i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r','s'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y','z']
             }
        res = ['']
        for i in digits:
            next_res = []
            for alp in d[i]:
                for tmp in res:
                    next_res.append(tmp+alp)
            res = next_res
        return res

    def letterCombinations_2(self, digits):
        res = []
        d = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']
             }

        def backtrace(combination, next_digits):
            if len(next_digits) == 0:
                res.append(combination)
            else:
                for letter in d[next_digits[0]]:
                    backtrace(combination+letter, next_digits[1:])
        if digits:
            backtrace('', digits)
        return res

s = Solution()
digits = '23'
print(s.letterCombinations_2(digits))

