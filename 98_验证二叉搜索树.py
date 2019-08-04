'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

不仅右子结点要大于该节点，整个右子树的元素都应该大于该节点，这意味着我们需要在遍历树的同时保留结点的上界与下界，在比较时不仅比较子结点的值，也要与上下界比较。
1. 中序遍历，那么得到的一定是有序的
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False

            if not helper(node.left, lower, node.val):
                return False

            if not helper(node.right, node.val, upper):
                return False
            return True

        return helper(root, float('-inf'), float('inf'))


s = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node2.left = node1
node2.right = node3

node5.left = node1
node5.right = node4
node4.left = node3
node4.rigth = node6

node7 = TreeNode(1)
node8 = TreeNode(1)
node7.left = node8
print(s.isValidBST(node7))
