'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 快慢指针+反转链表
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        slow = fast = head
        prev = None

        # 快慢指针找到链表中点
        while fast:
            slow = slow.next
            # 如果fast.next存在，就让fast = fast.next.next，否则fast = None
            fast = fast.next.next if fast.next else fast.next

        # 反转链表，以slow为头节点
        while slow:
            last = slow.next
            slow.next = prev
            prev = slow
            slow = last

        while head and prev:
            if head.val != prev.val:
                return False

            head = head.next
            prev = prev.next

        return True


node1 = ListNode(1)
node2 = ListNode(2)
# node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)

node1.next = node2
node2.next = node4
# node3.next = node4
node4.next = node5

s = Solution()
print(s.isPalindrome(node5))
