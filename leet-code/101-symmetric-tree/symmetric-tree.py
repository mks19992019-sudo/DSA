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

        def side_symmetric(node,reverse=False):
            list1 = []

            def check(node):
                if node ==None:
                    list1.append(None)
                    return

                list1.append(node.val)
                if reverse:
                    check(node.right)
                    check(node.left)
                    
                else:
                    check(node.left)
                    check(node.right)
                   
                    
            check(node)
            return list1
        
        left_side = side_symmetric(root.left)
        right_side = side_symmetric(root.right,True)

        if left_side == right_side:
            return True
        else:
            return False
            
        