class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        task = list(zip(difficulty,profit))
        task.sort()
        worker.sort()
        index, res, curr_max = 0, 0 ,0
        for w in worker:
            while index < len(task) and task[index][0] <=w:
                curr_max = max(curr_max,task[index][1])
                index+=1
            res+=curr_max
        return res


        