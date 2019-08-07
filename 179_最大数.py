'''
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
示例 1:
输入: [10,2]
输出: 210
示例 2:
输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
我们将整数转换成字符串后再进行比较，'3'+'30' = '330' > '30'+'3'='303'
'''


class Solution:
    def compStr(self, x, y):
        if x + y < y + x:
            return True
        else:
            return False

    def largestNumber(self, nums):
        if not nums:
            return ''
        nums = [str(num) for num in nums]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if self.compStr(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]

        # 如果nums里只有0，则只能输出一个0
        if nums[0] == '0':
            return '0'
        else:
            return ''.join(nums)


s = Solution()
nums = [0, 0]
print(s.largestNumber(nums))
