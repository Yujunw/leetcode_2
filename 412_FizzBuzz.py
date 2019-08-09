'''
写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
示例：
n = 15,
返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''


class Solution:
    def fizzBuzz(self, n: int):
        res = [str(i) for i in range(1, n + 1)]
        if n >= 3:
            res[2::3] = ['Fizz'] * len(res[2::3])
        if n >= 5:
            res[4::5] = ['Buzz'] * len(res[4::5])
        if n >= 15:
            res[14::15] = ['FizzBuzz'] * len(res[14::15])

        return res


s = Solution()
print(s.fizzBuzz(30))
