class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        task = list(zip(difficulty,profit))
        task.sort()
        max_heap = []

        index = 0
        res = 0
        worker.sort()
        for w in worker:
            while index < len(task) and task[index][0] <=w:
                heapq.heappush(max_heap,-task[index][1])
                index+=1
            if max_heap:
                print(w,index,max_heap[0])
                res-=max_heap[0]
        return res


        