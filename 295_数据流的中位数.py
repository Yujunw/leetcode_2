# -*- coding:utf-8 -*-
# Time:2019-08-24 10:37
# Author:june

'''
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
'''

import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = {}
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        self.d[self.count] = num

    def findMedian(self) -> float:
        return ()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

l = [1, 1, 3, 5, 2, 5, 8, 9, 6]
h = []
for i in l:
    heapq.heappush(h, i)

print(h)
