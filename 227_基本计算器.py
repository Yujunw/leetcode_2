'''
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
'''


class Solution:
    def calculate(self, s: str):
        if ' ' in s:
            s = ''.join(s.split(' '))
        print(s)

        i = 0
        while i < len(s):
            if s[i] == '*':
                temp = int(s[i - 1]) * int(s[i + 1])
                s = s.replace(s[i - 1:i + 2], str(temp))
                print(s)
            elif s[i] == '/':
                temp = int(s[i - 1]) // int(s[i + 1])
                s = s.replace(s[i - 1:i + 2], str(temp))
                print(s)
        return s

    def calculate_2(self, s: str):
        num_stack = []
        op_stack = []

        i = 0
        while i < len(s):
            if s[i] == ' ':
                continue

            if s[i].isdigit():
                num_stack.append(int(s[i]))
            elif s[i] in ['+', '-']:
                op_stack.append(s[i])
            elif s[i] == '*':




s = Solution()
strs = " 3+5 / 2 "
print(s.calculate(strs))
