# -*- coding:utf-8 -*-
# @Time    : 2019/8/23 15:29
# @Author  : Junwu Yu

'''
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞具有一个初始状态 live（1）即为活细胞， 或 dead（0）即为死细胞。
每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，
其中细胞的出生和死亡是同时发生的。

示例:

输入:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
'''


class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        flags = [[False] * col] * row
        print(flags)
        for i in range(row):
            for j in range(col):
                # 遍历周围8个位置
                count_1 = 0
                print('i,j:', i, j)
                print('第', i, j, '个 flags', flags[i][j])
                flags[i][j] = False
                for [x, y] in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    temp_x = i + x
                    temp_y = j + y
                    if 0 <= temp_x < row and 0 <= temp_y < col and board[temp_x][temp_y] == 1:
                        count_1 += 1
                        print('temp_x,temp_y:', temp_x, temp_y)
                print('count_1:', count_1)
                if board[i][j] == 1 and (count_1 < 2 or count_1 > 3):
                    flags[i][j] = True
                    print('1 changed')

                if board[i][j] == 0 and count_1 == 3:
                    flags[i][j] = True
                    print('0 changed')

                print('第', i, j, '个 flags', flags[i][j])
                print()

        print(flags)

        for i in range(row):
            for j in range(col):
                if flags[i][j]:
                    board[i][j] = 1 - board[i][j]

        print(board)

    def gameOfLife_2(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        flags = []
        print(flags)
        for i in range(row):
            for j in range(col):
                # 遍历周围8个位置
                count_1 = 0
                print('i,j:', i, j)
                for [x, y] in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    temp_x = i + x
                    temp_y = j + y
                    if 0 <= temp_x < row and 0 <= temp_y < col and board[temp_x][temp_y] == 1:
                        count_1 += 1
                        print('temp_x,temp_y:', temp_x, temp_y)
                print('count_1:', count_1)
                if board[i][j] == 1 and (count_1 < 2 or count_1 > 3):
                    flags.append(1)
                    print('1 changed')

                elif board[i][j] == 0 and count_1 == 3:
                    flags.append(1)
                    print('0 changed')
                else:
                    flags.append(0)

        for i in range(row):
            for j in range(col):
                if flags[i * col + j]:
                    board[i][j] = 1 - board[i][j]

        print(board)


s = Solution()
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
s.gameOfLife_2(board)
