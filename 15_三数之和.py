'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''


class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        length = len(nums)

        for i in range(length-2):
            if nums[i] > 0:
                return res
            # 必须得是nums[i] == nums[i-1]，可以跟后面的数字进行比较，与后面的重复，则当前这个不用比较，若是与前面的值相同，则继续，它的值可能会被j所用，例如[0,0,0]

            if i >=1 and nums[i] == nums[i-1]:
                continue

            j, k = i+1, length-1
            # print('?')
            while j < k:
                cur_sum = nums[i]+nums[j]+nums[k]

                if cur_sum == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif cur_sum > 0:
                    k -= 1
                    # 同理，必须要跟已经遍历过的元素进行比较
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                print('j,k',j,k)
        return res


s = Solution()
nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]

print(s.threeSum(nums))
