'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''

import math


class Solution:
    def countPrimes(self, n: int) -> int:
        # 时间复杂度过高
        count = 0
        for i in range(n):
            if self.isPrime(i):
                count += 1

        return count

    def isPrime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False

        return True

    def countPrimes_2(self, n: int) -> int:
        '''
        厄拉多塞筛法. 比如说求20以内质数的个数,首先0,1不是质数.2是第一个质数,然后把20以内所有2的倍数划去.2后面紧跟的数即为下一个质数3,
        然后把3所有的倍数划去.3后面紧跟的数即为下一个质数5,再把5所有的倍数划去.以此类推.
        :param n:
        :return:
        '''
        if n < 3:
            return 0
        output = [1] * n
        output[0], output[1] = 0, 0
        for i in range(2, int(n ** 0.5) + 1):
            if output[i] == 1:
                output[i * i:n:i] = [0] * len(output[i * i:n:i])
        return sum(output)


s = Solution()
n = 999983
print(s.countPrimes_2(n))
