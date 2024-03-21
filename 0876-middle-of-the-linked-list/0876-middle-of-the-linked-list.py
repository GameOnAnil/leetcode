# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        total = 0
        while head:
            total+=1
            head = head.next
        head = dummy
        for _ in range(total//2):
            head = head.next
        return head
        