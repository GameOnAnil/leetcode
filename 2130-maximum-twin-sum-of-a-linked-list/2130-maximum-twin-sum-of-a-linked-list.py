# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val
        dummy = head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
        res = 0
        while prev:
            res = max(res, prev.val + dummy.val)
            dummy = dummy.next
            prev = prev.next
        return res
