'''
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int):
        if not root:
            return None

        def inorder(root):
            if not root:
                return None

            stack = []
            if root.left:
                stack += inorder(root.left)
            stack.append(root.val)
            if root.right:
                stack += inorder(root.right)
            return stack

        stack = inorder(root)

        return stack[k - 1]
        # print(stack)


s = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node5.left = node3
node5.right = node6
node3.left = node2
node3.right = node4
node2.left = node1

print(s.kthSmallest(node5, 1))
