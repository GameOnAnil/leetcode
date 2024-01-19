class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        newbank = [item for item in bank if '1' in item]
        print(newbank)
        total = 0
        for i in range(1,len(newbank),1):
            m = newbank[i].count("1")
            n = newbank[i-1].count("1")
            total+=(m*n)
        return total