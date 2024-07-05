class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        INF = 10**6
        minDist = INF
        maxDist = 0
        previousCritical = None
        firstCritical = None
        prev = head
        curr = head.next
        count = 1

        while curr and curr.next:
            if (prev.val < curr.val and curr.val > curr.next.val) or (
                prev.val > curr.val and curr.val < curr.next.val
            ):
                if previousCritical is None:
                    previousCritical = count
                    firstCritical = count
                else:
                    minDist = min(count - previousCritical, minDist)
                    maxDist = max(count - firstCritical, maxDist)
                    previousCritical = count
            count += 1
            prev = curr
            curr = curr.next

        if previousCritical is None or minDist == INF:
            return [-1, -1]
        return [minDist, maxDist]