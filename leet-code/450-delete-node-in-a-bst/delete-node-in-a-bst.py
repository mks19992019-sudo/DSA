# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return
        
        if root.val == key:
            if root.left ==None and root.right ==None:
                return None
            if root.left and root.right:
                temp = root.left

                while temp.right:
                    temp = temp.right

                root.val = temp.val

                root.left = self.deleteNode(root.left,temp.val)
                return root
                



            if root.left:
                return root.left
            else:
                return root.right


        
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)

        return root
        


        