'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

位置i能接雨水的量为左边最大值与右边最大值中的最小值与高度的差
min(left_max, right_max) - height[i]
'''

class Solution:
    def trap(self, height):
        if len(height) < 2:
            return 0

        volume = 0
        max_height = max(height)
        max_height_index = height.index(max_height)

        left_max = height[0]
        for i in range(1, max_height_index):
            if left_max < height[i]:
                left_max = height[i]
            temp = min(left_max, max_height) - height[i]
            volume += temp

        right_max = height[-1]
        for j in range(len(height) - 2, max_height_index, -1):
            if height[j] > right_max:
                right_max = height[j]
            temp = min(right_max, max_height) - height[j]
            volume += temp

        return volume


s = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(s.trap(height))
