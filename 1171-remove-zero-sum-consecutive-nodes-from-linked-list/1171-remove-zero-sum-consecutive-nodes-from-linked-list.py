# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        data = []
        while head:
            data.append(head.val)
            head = head.next
        for i, m in enumerate(data):
            if m == 0:
                continue
            curr_sum = m
            for j in range(i + 1, len(data)):
                curr_sum += data[j]
                if curr_sum == 0:
                    data[i : j + 1] = [0] * (j + 1 - i)
        dummy = res = ListNode(None)
        for d in data:
            if d == 0:
                continue
            if res.val == 0:
                res.val = d
            else:
                res.next = ListNode(d)
                res = res.next
        return  dummy.next
