'''
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        最直白的方法，将每个链表的转换成数字，相加后又转换成链表
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_num = self.node2num(l1)
        l2_num = self.node2num(l2)
        res = l1_num + l2_num
        # print(res)
        l0 = ListNode(0)
        dummy = l0
        if res == 0:
            return dummy
        while res:
            tmp = res % 10
            res = res // 10
            ll = ListNode(tmp)
            l0.next = ll
            l0 = l0.next

        return dummy.next

    def node2num(self, l):
        num = 0
        i = 0
        while l:
            num += l.val * 10 ** i
            l = l.next
            i += 1
        return num

    def addTwoNumbers_2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = p0 = ListNode(0)
        p1, p2 = l1, l2
        carry = 0
        while p1 or p2:
            s = p1.val + p2.val
            s = s % 10 + carry
            p0.next = ListNode(s)
            p0 = p0.next
            carry = s // 10

            p1 = p1.next
            p2 = p2.next

        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)

    l0 = ListNode(0)

    l1.next = l2
    l2.next = l3

    l4.next = l5
    l5.next = l6
    s = Solution()
    l = s.addTwoNumbers(l0, l0)

    while l:
        print(l.val)
        l = l.next
