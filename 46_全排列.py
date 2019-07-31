'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

回溯算法，套模板
'''


class Solution:
    def permute(self, nums):
        # if not nums:
        #     return []
        res = []

        def _backtrace(combination, digits):
            # 找到一个终结递归的方式
            if len(digits) == 0:
                res.append(combination)
            else:
                # 在这里开始递归
                for i in digits:
                    temp = [j for j in digits if j != i]
                    _backtrace(combination + [i], temp)

        if nums:
            _backtrace([], nums)

        return res


S = Solution()
nums = [1, 2, 4, 3]
print(S.permute(nums))
