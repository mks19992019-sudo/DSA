# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.ans = None

        def inorder(root,k):
            if root is None or self.ans != None:
                return 
            
            inorder(root.left,k)

            self.count +=1

            if self.count == k:
                self.ans = root.val
                return 
            inorder(root.right,k)
        inorder(root,k)
        return self.ans
            

        