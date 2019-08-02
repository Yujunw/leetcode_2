'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    def generate(self, numRows):
        if numrows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]
        for row in range(2, numRows):
            temp = [1]
            for col in range(1, row):
                temp.append(res[row - 1][col - 1] + res[row - 1][col])
            temp.append(1)
            res.append(temp)
        return res


s = Solution()
numrows = 6
print(s.generate(numrows))
