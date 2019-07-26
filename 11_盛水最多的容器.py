'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''

class Solution:
    def maxArea(self, height):
        length = len(height)
        if length < 2:
            return 0
        maxarea = 0
        i = 0
        j = length - 1

        while i < j:
            if height[i] < height[j]:
                area = height[i] * (j - i)
                if area > maxarea:
                    maxarea = area
                i += 1
            else:
                area = height[j] * (j - i)
                if area > maxarea:
                    maxarea = area
                j -= 1

        return maxarea

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
area = s.maxArea(height)
print(area)


