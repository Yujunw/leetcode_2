'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28

总共要走(m-1)+（n-1）步，其中（n-1）步是向右走，方法共有C(m+n-2)(n-1)种
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        up, down = 1, 1
        for i in range(m, m + n - 1):
            up = up * i

        for j in range(1, n):
            down = down * j

        return up / down


s = Solution()
m = 7
n = 3
print(s.uniquePaths(m, n))
