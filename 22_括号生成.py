'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
回溯法可以被认为是一个有过剪枝的DFS过程
生成各种组合的题目就使用回溯算法，深度优先搜索
控制右括号的个数必须小于左括号
'''

class Solution:
    def generateParenthesis(self, n):
        res = []
        def backtrace(combination, left, right):
            if len(combination) == 2*n:
                res.append(combination)
            # 这就是剪枝条件，左括号个数必须小于总数，右括号个数必须小于左括号
            if left < n:
                backtrace(combination+'(', left+1, right)
            if right < left:
                backtrace(combination+')', left, right+1)

        backtrace('',0,0)
        return res

S = Solution()
n = 0
print(S.generateParenthesis(n))

        

