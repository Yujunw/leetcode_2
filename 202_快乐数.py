'''
一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 

输入: 19
输出: true
解释:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

所有非快乐数最后会陷入循坏 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        res = set()
        while n != 1:
            s = 0
            while n:
                temp = n % 10
                n = n // 10
                s += temp ** 2
            n = s
            if s in res:
                return False
            else:
                res.add(s)

        return True


s = Solution()
print(s.isHappy(5))
