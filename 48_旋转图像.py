'''
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
'''
import math
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        m = math.ceil(n / 2)

        for i in range(m):
            for j in range(n // 2):
                temp = [0] * 4
                row, col = i, j
                # 存储4个元素
                for k in range(4):
                    temp[k] = matrix[row][col]
                    row, col = col, n - 1 - row
                # 旋转4个元素
                for k in range(4):
                    matrix[row][col] = temp[(k - 1) % 4]
                    row, col = col, n - 1 - row

        print(matrix)



S = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
S.rotate(matrix)
