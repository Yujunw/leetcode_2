'''
打乱一个没有重复元素的数组。

// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();

'''
import random
import copy


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.list = nums
        self.orig_list = copy.deepcopy(self.list)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """

        return self.orig_list

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.list)
        return self.list


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
obj = Solution(nums)

param_1 = obj.reset()
print(param_1)

param_2 = obj.shuffle()
print(param_2)

param_3 = obj.reset()
print(param_3)
