class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        res = 0
        def generateSubset(index,path):
            if index == len(nums):
                subsets.append(path[:])
                return

            path.append(nums[index])
            generateSubset(index+1,path)
            path.pop()

            generateSubset(index+1,path)

        generateSubset(0,[])

        for s in subsets:
            curr = 0
            for i in s:
                curr^=i
            res+=curr
        return res
        