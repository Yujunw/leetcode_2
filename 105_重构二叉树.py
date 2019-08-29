'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        # preorder = preorder[1:]

        if index < 1:
            root.left = None
        else:
            root.left = TreeNode(inorder[index-1])

        if index == len(preorder)-1:
            root.right = None
        else:
            root.right = TreeNode(inorder[index+1])

    def buildTree_2(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        # 在中序遍历中，说明index前面都是左子树节点，index后面都是右子树节点
        # 在先序遍历中，index的大小即为左子树节点个数，之后都是右子节点
        index = inorder.index(preorder[0])

        root.left = self.buildTree_2(preorder[1:index+1],inorder[0:index])
        root.right = self.buildTree_2(preorder[index+1:], inorder[index+1:])
        return root

    def inorderTravel(self, root):
        if not root:
            return []
        res = []

        res += self.inorderTravel(root.left)
        res.append(root.val)
        res += self.inorderTravel(root.right)

        return res

s = Solution()
preorder = [3,9,6,15,7,8]
inorder = [6,9,3,7,15,8]
root = s.buildTree_2(preorder, inorder)
print(s.inorderTravel(root))
