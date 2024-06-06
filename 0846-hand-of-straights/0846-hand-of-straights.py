class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        print(count)
        for i in sorted(count.keys()):
            if count[i] <=0:
                continue
            for j in range(groupSize)[::-1]:
                index = i + j
                # print(i,index)
                count[index]-=count[i]
                if count[index] < 0:
                    return False
        return True