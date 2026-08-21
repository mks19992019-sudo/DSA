# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """


        def check(left, right):

            if left == None and right == None:
                return True

            if left == None or right == None:
                return False

            if left.val != right.val:
                return False

            return check(left.left, right.right) and check(left.right, right.left)

        

        ans = check(root.left,root.right)  
        return ans      
                    

        
            
        