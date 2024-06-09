class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()  
        ans = {0}  
        for r in rewardValues:
            new_rewards = set()
            for x in ans:
                # print("LPP",x)
                if r > x:
                    new_rewards.add(x + r)
            ans.update(new_rewards)
            # print(ans)
        
        return max(ans)