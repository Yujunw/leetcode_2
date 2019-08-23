'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。
示例 1:
输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

求图中连通块的数量
并查集，bfs，dfs
'''


class Solution:

    def numIslands(self, grid):
        f = {}

        def find(x):
            # 若在f的键中没有x，则默认设置f[x]=x
            f.setdefault(x, x)

            if f[x] != x:
                f[x] = find(f[x])
            return f[x]


s = Solution()
s.numIslands(1)
