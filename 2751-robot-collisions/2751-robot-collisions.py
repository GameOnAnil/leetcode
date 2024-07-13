class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        indices.sort(key=lambda x: positions[x])
        stack = []
        for curr in indices:
            if directions[curr] == "R":
                stack.append(curr)
            else:
                while stack and healths[curr] > 0:
                    prev = stack.pop()
                    if healths[curr] > healths[prev]:
                        healths[prev] = 0
                        healths[curr]-=1
                    elif healths[curr] < healths[prev]:
                        healths[curr] = 0
                        healths[prev]-=1
                        stack.append(prev)
                    else:
                        healths[curr] = 0
                        healths[prev] = 0
        res= []
        for h in healths:
            if h > 0:
                res.append(h)
        return res
