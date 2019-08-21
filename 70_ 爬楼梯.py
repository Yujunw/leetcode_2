'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

设爬 n个台阶有 f(n) 种可能：
假设先爬1阶，剩下n-1 阶有f(n-1) 种可能；
假设先爬2阶，剩下 n-2阶有 f(n-2) 种可能，
因此爬n阶可以转化为两种爬n-1阶问题之和：f(n) = f(n-1) + f(n-2)；
初始状态: 第一次爬1阶，f(1)=1；第一次爬2阶，f(2) = 2
动态方程: f(n) = f(n-1) + f(n-2)
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        first, second = 1, 2
        res = 0
        while n - 2:
            res = first + second
            first = second
            second = res
            n -= 1
        return res


S = Solution()
n = 5
print(S.climbStairs(n))
