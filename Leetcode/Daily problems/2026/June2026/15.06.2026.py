# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        if n == 1:
            return None
        m = n//2
        curr = head
        while m:
            m -= 1
            if m==0:
                curr.next = curr.next.next
            curr = curr.next
        return head
