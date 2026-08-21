# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """



        def check(tree_1,tree_2):
            if tree_1 ==None and tree_2==None:
                return True
                
            if tree_1 ==None or tree_2 ==None:
                return False            
            if tree_1.val != tree_2.val:
                return False
                
            return check(tree_1.left,tree_2.left) and check(tree_1.right,tree_2.right)
            
        ans = check(p,q)
        return ans


            
        
     




        

            

        

        
        
            
            
        