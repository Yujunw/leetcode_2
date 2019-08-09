'''
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。
'''


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root.left and not root.right:
            return None

        root.left.next = root.right
        if root.left.right:
            root.left.right.next = root.right.left
        self.connect(root.left)
        self.connect(root.right)

    def connect_2(self, root):
        if not root:
            return None

        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

        self.connect_2(root.left)
        self.connect_2(root.right)
        return root
