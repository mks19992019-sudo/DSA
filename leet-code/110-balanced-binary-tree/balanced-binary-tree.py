# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def check_balanced(root):
            if root == None:
                return 0

            ls = check_balanced(root.left)
            rs = check_balanced(root.right)
        
            if ls is False or rs is False:
                return False
            if abs(ls-rs) > 1:
                return False
        
            return max(ls,rs)+1
        ans = check_balanced(root)
        if ans is False:
            return False
        else:
            return True
       
        

        
        