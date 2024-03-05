class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 0:
            return 0
        if len(fruits) == 1:
            return 1
        l, r = 0, 0
        basket = defaultdict(int)
        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            if len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
        return r - l + 1
