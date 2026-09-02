# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = []

        def inorder(root):
            if root ==None:
                return 
            
            inorder(root.left)
            node.append(root)
            inorder(root.right)

        inorder(root)

        values = []
        for val in node:
            values.append(val.val)
        
        values.sort()

        for i in range(len(node)):
            node[i].val = values[i]



        