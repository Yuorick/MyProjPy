# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        lsRez = []
        def inorder(root):
            if root:
                inorder(root.left)
                lsRez.append(root.val)
                inorder(root.right)
        inorder(root)
        return lsRez

nd0 = TreeNode(0, None, 1)
nd1 = TreeNode(1, 0, 3)
nd2 = TreeNode(3,1, 5)
root = [nd0, nd1, nd2]
olen = len(root)

solv = Solution()
solv.inorderTraversal(root)