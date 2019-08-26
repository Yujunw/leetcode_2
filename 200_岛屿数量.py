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
            # find(x), 找到x的第一个祖先
            # 若在f的键中没有x，则默认设置f[x]=x
            f.setdefault(x, x)

            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            # 将y的祖先变成x的祖先
            f[find(x)] = find(y)

        if not grid:
            return 0

        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    for [x, y] in [[1, 0], [0, 1]]:
                        temp_x = i + x
                        temp_y = j + y
                        if 0 <= temp_x < row and 0 <= temp_y < col and grid[temp_x][temp_y] == '1':
                            # 不能这样使用，因为grid元素只有0和1，字典键肯定会重复，因此使用序号做键
                            # union(grid[temp_x][temp_y],grid[i][j])
                            union(temp_x * col + temp_y, i * col + j)

        res = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res.add(find(i * col + j))

        return len(res)


s = Solution()
grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
grid1 = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
print(s.numIslands(grid1))
