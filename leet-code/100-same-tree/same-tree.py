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

        def values(node):
            list1 = []
            def check(node):
                if node == None:
                    list1.append(None)
                    return 
                list1.append(node.val)

                check(node.left)
                check(node.right)
            check(node)
            return list1
            
        
        arr1 = values(p)
        arr2 = values(q)

        if arr1 == arr2:
            return True
        else:
            return False


        

            

        

        
        
            
            
        