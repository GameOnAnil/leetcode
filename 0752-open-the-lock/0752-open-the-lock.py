class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        q = deque()
        q.append(("0000",0))
        visited = set("0000")

        while q:
            curr, count = q.popleft()
            if curr == target:
                return count
            
            if curr in deadends:
                continue
            for i in range(4):
                digits = int(curr[i])
                for d in [-1, 1]:
                    new_digit = (digits+ d) % 10
                    newStr = curr[:i] + str(new_digit) + curr[i + 1 :]

                    if newStr not in visited:
                        visited.add(newStr)
                        q.append((newStr, count + 1))
        return -1
