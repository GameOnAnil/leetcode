# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        curr = prev.next
        prev.next = None
        while curr:
            temp = curr.next
            if curr.val >= prev.val:
                curr.next = prev
                prev = curr
            curr = temp
        return prev
