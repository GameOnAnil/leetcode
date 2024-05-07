# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = []
        while head:
            num.append(str(head.val))
            head = head.next
        doublenum = str(int("".join(num)) * 2)
        dummy = curr = ListNode()
        for i in doublenum:
            curr.next = ListNode(int(i))
            curr = curr.next
        return dummy.next



        
        