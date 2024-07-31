class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def helper(i):
            if i == len(books):
                return 0
            curr_width = shelfWidth
            max_height = 0
            res = float("inf")
            for j in range(i,len(books)):
                width, height = books[j]
                if curr_width < width:
                    break
                curr_width -= width
                max_height = max(max_height,height)
                res = min(res, helper(j+1) + max_height)
            return res

        return helper(0)
        