# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy

        carry = 0


        while l1 or l2 or carry:

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry

            carry = total //10
            node_val = total%10

            current.next = ListNode(node_val)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
        return dummy.next


        