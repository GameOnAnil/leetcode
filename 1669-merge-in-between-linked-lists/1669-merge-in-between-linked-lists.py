# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l,r = None,None
        head = list1
        index = 0
        while list1.next:
            if (index + 1) == a:
                l = list1
            if index == b:
                r = list1.next
                list1 = l
                list1.next = list2
                while list1.next:
                    list1 = list1.next
                list1.next = r
                break
            list1 = list1.next
            index+=1
        return head
        