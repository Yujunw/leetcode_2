'''
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
'''

class Solution:
    def intersect(self, nums1, nums2):
        res = []
        nums1.sort()
        nums2.sort()
        # length = len(nums1) if len(nums1) < len(nums2) else len(nums2)
        i,j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1

        return res

s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(s.intersect(nums1, nums2))

