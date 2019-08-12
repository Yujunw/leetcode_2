'''
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

把数组的索引号利用起来,如果我们把位置0我们放数字1,位置1我们放数字2...我们就可以节省存储索引的空间了,
按照这样的方法重新整理数组,我们再扫一次就能知道答案了.
'''


class Solution:
    def firstMissingPositive(self, nums):
        length = len(nums)

        for i in range(length):
            while 1 <= nums[i] <= length and nums[i] != nums[nums[i] - 1]:
                #  说明并不是同时进行的，先让nums[i]的值等于nums[nums[i] - 1]，此时数组nums已经发生了变化，nums[i]的值改变了，
                #  因此nums[nums[i] - 1]不是之前的那个nums[nums[i] - 1]
                t = nums[i]
                nums[i], nums[t - 1] = nums[t - 1], nums[i]
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i] 错误
                # nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] 正确

        j = 0
        while j < length:
            if nums[j] != j + 1:
                return j + 1
            j += 1

        return j + 1

    def fun(self, nums):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        print(nums)
        i = 0
        while i < n and i + 1 == nums[i]:
            i += 1
        return i + 1


s = Solution()
nums = [3, 4, -1, 1]
print(s.firstMissingPositive(nums))
