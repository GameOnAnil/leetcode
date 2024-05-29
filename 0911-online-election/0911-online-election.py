class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leader = []
        self.count = defaultdict(int)
        self.max = -1
        self.times = times
        for time, person in zip(times,persons):
            self.count[person]+=1
            if self.max <= self.count[person]:
                self.max = self.count[person]
                self.leader.append((time,person))
        print(self.leader)

    def q(self, t: int) -> int:
        index =0
        l,r = 0, len(self.leader) - 1
        while l<=r:
            index= (l+r)//2
            if t == self.leader[index][0]:
                return self.leader[index][1]
            elif t < self.leader[index][0]:
                r = index -1
            else:
                l = index + 1
        return self.leader[r][1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)