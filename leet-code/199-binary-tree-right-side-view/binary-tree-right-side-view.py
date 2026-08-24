# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None:
            return []

        queu = deque()
        queu.append(root)

        ans = []
        while queu:
            temp = []
            for i in range(len(queu)):
                q = queu.popleft()
                temp.append(q.val)
                if q.left !=None:
                    queu.append(q.left)
                if q.right != None:
                    queu.append(q.right)
            ans.append(temp[-1])
        return ans







        