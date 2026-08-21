# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def min_length(node):
            if node ==None:
                return 0
            
            LS = min_length(node.left)
            RS = min_length(node.right)

            if node.left == None:
                return RS +1
            if node.right ==None:
                return LS +1

            minum = min(LS,RS)+1

            return minum
        ans = min_length(root)

        return ans
        