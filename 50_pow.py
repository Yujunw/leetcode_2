'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 时间复杂度为O(N)
        flag = 1 if n >= 0 else -1
        n = abs(n)
        s = 1
        while n:
            s = s * x
            n -= 1
        if flag == 1:
            return s
        else:
            return 1 / s

    def myPow_2(self, x: float, n: int) -> float:
        # 递归调用，时间复杂度O(logN)
        if n == 0:
            return 1

        flag = 1 if n >= 0 else -1
        n = abs(n)

        half = self.myPow_2(x, n // 2)
        if n % 2 == 0:
            res = half * half
        else:
            res = half * half * x
        if flag == 1:
            return res
        else:
            return 1 / res


S = Solution()
x, n = 2.1, -2
print(S.myPow_2(x, n))
