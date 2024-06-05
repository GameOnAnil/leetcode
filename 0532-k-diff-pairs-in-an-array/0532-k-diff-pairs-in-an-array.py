class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        @cache
        def find_index(curr,i):
            l,r = 0, len(nums) -1 
            while l<=r:
                mid = (l+r) // 2
                if mid !=curr and  nums[mid] == i:
                    return mid
                elif nums[mid] < i:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
                
        seen = set()
        res = 0
        for i,v in enumerate(nums):
            index = find_index(i,v+k)
            if index == -1:
                continue

            if (nums[i],nums[index]) not in seen and (nums[index],nums[i]) not in seen:
                # print(nums[i],nums[index])
                res+=1
                seen.add((nums[i],nums[index]))
        return res
        