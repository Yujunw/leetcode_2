'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

如果二叉树对称，那么左右子树也对称
构建一个match函数，通过深度优先遍历DFS判断是否为对称二叉树，思路是在遍历过程中，每次对比当前点与对称点的值是否相等。
参数：
节点l节点r，每轮递归比较两节点值是否相等l.val == r.val；
返回值：
节点l和r值是否相等 且
节点l的左子树和节点r右子树是否对称 且
节点l的右子树和节点r左子树是否对称
终止条件：
节点l和r同时为null则返回true，代表同时越过叶子节点，以上全部值相同；
节点l和r有一个为null则返回false，代表只有一边越过叶子节点，意味着树不对称。

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def __equal(left, right):
            if not left and not right:
                return True
            # 经过前面的判断之后，left和right必有一个存在
            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return __equal(left.left, right.right) and __equal(left.right, right.left)

        return __equal(root.left, root.right)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(4)
node5 = TreeNode(6)
node6 = TreeNode(9)
node7 = TreeNode(4)
node8 = TreeNode(8)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

s = Solution()
print(s.isSymmetric(node1))
