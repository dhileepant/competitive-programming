# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        d = []
        p = head.val
        head = head.next
        i = 2
        while head:
            if not head.next:
                break
            curr = head.val
            n = head.next.val
            if (p > curr and curr < n) or (p < curr and curr > n):
                d.append(i)
            p = curr
            head = head.next
            i += 1
        if len(d) < 2:
            return [-1, -1]
        mx = d[-1] - d[0]
        mn = 10 ** 7
        for j in range(len(d)-1):
            mn = min(mn, d[j+1] - d[j])
        # print(d)
        return [mn, mx]
