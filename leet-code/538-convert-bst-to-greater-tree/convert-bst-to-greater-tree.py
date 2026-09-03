# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.sum = 0
        def helper(root):
 
            if root == None:
                return
            helper(root.right)

            root.val = root.val + self.sum
            self.sum = root.val

            helper(root.left)

        helper(root)
        return root



            
        