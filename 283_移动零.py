'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

双指针，一个指针指向0，另一个指针遍历数组，遇到非0元素则进行交换
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

    def moveZeros_2(self, nums):
        i = 0
        # i是第一个0的位置，i<len(nums)

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return nums


s = Solution()
nums = [1]
print(s.moveZeros_2(nums))
