# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return None

        vist = set()
        temp = head 


        while temp!=None:
            if temp in vist:
                return True
            vist.add(temp)
            temp = temp.next
        
        return False








        