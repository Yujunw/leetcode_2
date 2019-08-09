'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代法
        # if not head or not head.next:
        #     return head
        prev = None
        while head:
            last = head.next
            head.next = prev
            prev = head
            head = last
        return prev

    def reverseList_2(self, head: ListNode) -> ListNode:
        # 递归法
        if not head or not head.next:
            return head

        newHead = self.reverseList_2(head.next)
        head.next.next = head
        head.next = None
        return newHead


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
pointer = s.reverseList_2(node5)
while pointer:
    print(pointer.val)
    pointer = pointer.next
