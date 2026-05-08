# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find total length
        ptr = head
        total_length = 0
        while ptr:
            total_length += 1
            ptr = ptr.next
        
        if total_length-n == 0:
            return head.next

        # find the (total length - n - 1) node
        ptr = head
        for i in range(1, total_length-n):
            ptr = ptr.next

        # ptr.next = ptr.next.next if n > 0 else None
        ptr.next = ptr.next.next
        return head