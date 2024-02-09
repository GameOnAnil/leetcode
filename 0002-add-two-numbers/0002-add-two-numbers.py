# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1, sum2 = "",""
        while l1:
            sum1=str(l1.val)+ sum1
            l1 = l1.next
        while l2:
            sum2=str(l2.val)+ sum2
            l2 = l2.next
        total = str(int(sum1)+int(sum2))
        prev_node = None
        for i in total:
            node = ListNode(int(i))
            node.next = prev_node
            prev_node = node
        return prev_node
