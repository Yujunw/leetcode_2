'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                for j in range(len(nums) - 1 - count_0):
                    nums[j] = nums[j + 1]
                nums[-1] = 0
                count_0 += 1
        print(nums)


s = Solution()
nums = [0, 1, 0, 3, 12]
