# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        prev = dummy
        prev.next = head

        while prev.next and prev.next.next:
            first = prev.next
            sec = prev.next.next

            first.next = sec.next
            sec.next = first
            prev.next = sec

            prev = first
            
        return dummy.next

        