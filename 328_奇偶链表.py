'''
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
示例 1:
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:
输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL
说明:
应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        p = odd = ListNode(-1)
        q = even = ListNode(-1)
        while head:
            print('head', head.val)
            odd.next = head
            odd = odd.next
            head = head.next
            # print('head', head.val)
            if not head:
                break
            print('head', head.val)
            even.next = head
            even = even.next
            head = head.next

        while p:
            print('p', p.val)
            p = p.next

        while q:
            print('q', q.val)
            q = q.next
        # odd.next = q.next
        # return p.next


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
node = s.oddEvenList(node1)
while node:
    print(node.val)
    node = node.next

if not None:
    print(999)
