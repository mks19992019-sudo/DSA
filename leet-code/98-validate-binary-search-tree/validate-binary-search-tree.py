# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node,left,right):
            if node ==None:
                return True
            
            if node.val >= right or node.val <= left:
                return False
            ls = check(node.left,left,node.val)
            rs = check(node.right,node.val,right)

            if ls is True and rs is True:
                return True
            else:
                return False
        ans =  check(root,-float('inf'),float('inf'))
        return ans


        
        