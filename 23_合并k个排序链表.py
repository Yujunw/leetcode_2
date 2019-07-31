'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''


# 在leetcode-cn中必须使用python2才能通过
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 普通的队列是一种先进先出的数据结构，元素在队列尾追加，而从队列头删除。在优先队列中，元素被赋予优先级。当访问元素时，具有最高优先级的元素最先删除。
# 优先队列具有最高级先出 （first in, largest out）的行为特征。通常采用堆数据结构来实现
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists):
        dummy = head = ListNode(0)
        q = PriorityQueue()

        # 将每个链表的头节点都存储到q中
        for l in lists:
            if l:
                q.put((l.val, l))

        while not q.empty():
            # 在所有的头节点中,先出去一个val最小的
            val, node = q.get()
            head.next = ListNode(val)
            head = head.next
            node = node.next
            # 出去val最小的之后,再put其后面的一个节点,与之前的节点进行比较大小
            if node:
                q.put((node.val, node))
        return dummy.next


s = Solution()
node0 = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

node8 = ListNode(8)

node0.next = node2
# node2.next = node4

node1.next = node3
node3.next = node5
node5.next = node7

node4.next = node6

q = s.mergeKLists([node0, node8, node1, node4])
while q:
    print(q.val)
    q = q.next
