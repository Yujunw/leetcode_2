'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None

        head = dummy = ListNode(0)

        while l1 and l2:
            if l1.val > l2.val:
                head.next = ListNode(l2.val)
                l2 = l2.next
            else:
                head.next = ListNode(l1.val)
                l1 = l1.next
            head = head.next

        if l1:
            head.next = l1
        if l2:
            head.next = l2

        return dummy.next


s = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node6 = ListNode(1)
node7 = ListNode(3)
node8 = ListNode(4)

node1.next = node2
node2.next = node4
# node5.next = node7

node6.next = node7
node7.next = node8
# node6.next = node8

head =s.mergeTwoLists(node1, node6)
while head:
    print(head.val)
    head = head.next
