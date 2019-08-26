# -*- coding:utf-8 -*-
# @Time    : 2019/8/26 20:16
# @Author  : Junwu Yu

'''
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
'''


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            # 将y的祖先变成x的祖先
            f[find(x)] = find(y)

        row, col = len(board), len(board[0])

        if not board:
            return

        dummy = row * col
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(i * col + j, dummy)
                    for [x, y] in [[1, 0], [0, 1]]:
                        temp_x = x + i
                        temp_y = y + j

                        if 0 < temp_x < row - 1 and 0 < temp_y < col - 1:
                            union(i * col + j, temp_x * col + temp_y)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    if find(board[i][j]) == find(i * col + j):
                        board[i][j] = 'X'

        return board


s = Solution()
grid = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
print(s.solve(grid))
