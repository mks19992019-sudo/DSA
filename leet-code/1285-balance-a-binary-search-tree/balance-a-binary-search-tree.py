# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        ans = []

        def inorder(root):
            if root ==None:
                return 
            inorder(root.left)
            ans.append(root)
            inorder(root.right)
        
        inorder(root)

        def helper(left,right):
            if left > right:
                return None
            mid = (left+right)//2
            root = ans[mid]

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root


        return helper(0, len(ans) - 1)


        