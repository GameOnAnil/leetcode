# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        curr = head
        length = 0
        while curr:
            length+=1
            curr = curr.next
        mid = length // 2
        for _ in range(mid):
            head = head.next
        return head

        