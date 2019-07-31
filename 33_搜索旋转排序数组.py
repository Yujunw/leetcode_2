'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
'''


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == target:
                return i
            else:
                i += 1
            if nums[j] == target:
                return j
            else:
                j -= 1
        return -1

    def search_2(self, nums, target):
        mid = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                mid = i + 1
                break
        print(mid)


S = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 1
print(S.search_2(nums, target))
