# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode()
        odd = ListNode()
        evenHead = even
        oddHead = odd
        isOdd = True
        while head:
            if isOdd:
                odd.next = ListNode(head.val)
                odd = odd.next
                isOdd= False
            else:
                even.next = ListNode(head.val)
                even = even.next
                isOdd = True
            head = head.next
        dummy = oddHead.next
        while oddHead.next:
            oddHead = oddHead.next
        oddHead.next = evenHead.next
        return dummy

        