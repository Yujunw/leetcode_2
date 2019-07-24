'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        时间复杂度 O(n^2)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length < 2:
            return None

        for i in range(length-1):
            for j in range(i+1,length):
                if nums[i]+nums[j] == target:
                    return [i,j]

        return None

    def twoSum_2(self, nums, target):
        length = len(nums)
        if length < 2:
            return None
        d = {}
        for index, element in enumerate(nums):
            another_num = target - nums[index]

            for key, value in d.items():
                if another_num == value:
                    return [key,index]
            d[index] = element
        return None

    def twoSum_3(self, nums, target):
        '''
        时间复杂度最低 O(n)，关键是在写入字典的时候，键和值是反过来的
        '''
        length = len(nums)
        if length < 2:
            return None

        d = {}
        for index, element in enumerate(nums):
            another_num = target - nums[index]

            # 时间复杂度O(1)
            if another_num in d.keys():
                return [d[another_num], index]
            else:
                d[element] = index

        return None


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum_3(nums, target))


