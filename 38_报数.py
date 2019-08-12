'''
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。
'''


class Solution:
    def countAndSay(self, n: int):
        def next_num(num):
            res = ''
            i = 0
            length = len(num)
            while i < length:
                count = 1
                while i < length - 1 and num[i] == num[i + 1]:
                    count += 1
                    i += 1
                res += str(count) + str(num[i])
                i += 1

            return res

        # 不断地根据前一个数字推出后一个数字
        res = '1'
        for i in range(1, n):
            res = next_num(res)
        return res


s = Solution()
s.countAndSay(10)
