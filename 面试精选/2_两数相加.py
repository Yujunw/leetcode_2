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
        l1_num = self._node2num(l1)
        l2_num = self._node2num(l2)
        res = l1_num+l2_num
        # print(res)
        l0 = ListNode(0)
        dummy = l0
        if res == 0:
            return dummy
        while res:
            tmp = res%10
            res = res//10
            ll = ListNode(tmp)
            l0.next = ll
            l0 = l0.next

        return dummy.next

    def _node2num(self, l):
        num = 0
        i=0
        while l:
            num += l.val*10**i
            l = l.next
            i += 1
        return num

    def addTwoNumbers_2(self, l1, l2):
        """
        伪代码如下：

        将当前结点初始化为返回列表的哑结点。
        将进位 carrycarry 初始化为 00。
        将 pp 和 qq 分别初始化为列表 l1l1 和 l2l2 的头部。
        遍历列表 l1l1 和 l2l2 直至到达它们的尾端。
        将 xx 设为结点 pp 的值。如果 pp 已经到达 l1l1 的末尾，则将其值设置为 00。
        将 yy 设为结点 qq 的值。如果 qq 已经到达 l2l2 的末尾，则将其值设置为 00。
        设定 sum = x + y + carrysum=x+y+carry。
        更新进位的值，carry = sum / 10carry=sum/10。
        创建一个数值为 (sum \bmod 10)(summod10) 的新结点，并将其设置为当前结点的下一个结点，然后将当前结点前进到下一个结点。
        同时，将 pp 和 qq 前进到下一个结点。
        检查 carry = 1carry=1 是否成立，如果成立，则向返回列表追加一个含有数字 11 的新结点。
        返回哑结点的下一个结点。

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = p0 = ListNode(0)
        p1, p2 = l1, l2
        carry = 0
        while p1 or p2:
            s = p1.val + p2.val + carry
            carry = s // 10
            s = s % 10
            p0.next = ListNode(s)
            p0 = p0.next

            p1 = p1.next
            p2 = p2.next

            if not p1 and p2:
                p1 = ListNode(0)
            if p1 and not p2:
                p2 = ListNode(0)

        if carry == 1:
            p0.next = ListNode(1)
        return dummy.next



if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)

    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    l7 = ListNode(7)
    l9 = ListNode(9)

    l0 = ListNode(0)

    l2.next = l4
    l4.next = l3

    # l5.next = l6
    # l6.next = l4
    # l6.next = l5

    s = Solution()
    l = s.addTwoNumbers_2(l5,l5)

    while l:
        print(l.val)
        l = l.next
