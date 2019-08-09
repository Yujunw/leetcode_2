'''
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2
        head = TreeNode(nums[mid])
        head.left = self.sortedArrayToBST(nums[:mid])
        head.right = self.sortedArrayToBST(nums[mid + 1:])
        return head

    def traversalTres(self, root):
        if not root:
            return []
        res = []
        res.append(root.val)
        res += self.traversalTres(root.left)
        res += self.traversalTres(root.right)
        return res


# node1 = TreeNode(0)
# node2 = TreeNode(-3)
# node3 = TreeNode(9)
# node4 = TreeNode(-10)
# node5 = TreeNode(5)
#
# node1.left = node2
# node1.right = node3
# node2.left = node4
# node3.left = node5

s = Solution()
nums = [-10, -3, 0, 5, 9]
root = s.sortedArrayToBST(nums)
print(s.traversalTres(root))
