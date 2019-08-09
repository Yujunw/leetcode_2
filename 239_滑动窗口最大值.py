'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。
示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
import heapq
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        for i in range(len(nums) - k + 1):
            max_v = heapq.nlargest(1, nums[i:i + k])
            res += max_v
        return res

    def fun(self, nums, k):
        '''
        双向队列
        1. 处理前 k 个元素，初始化双向队列。
        2. 遍历整个数组。在每一步 :
            清理双向队列 :
            - 只保留当前滑动窗口中有的元素的索引。
            - 移除比当前元素小的所有元素，它们不可能是最大的。
        3. 将当前元素添加到双向队列中。
        4. 将 deque[0] 添加到输出中。
        5, 返回输出数组。
        '''
        if k == 0:
            return []
        if k == 1:
            return nums
        queue = deque()
        n = len(nums)

        # 参数是索引
        def clean_deque(i):
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

        max_idx = 0
        for i in range(k):
            clean_deque(i)
            queue.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        for i in range(k, n):
            clean_deque(i)
            queue.append(i)
            output.append(nums[queue[0]])

        return output


s = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(s.maxSlidingWindow(nums, k))
