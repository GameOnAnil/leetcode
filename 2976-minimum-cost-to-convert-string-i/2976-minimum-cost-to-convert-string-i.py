class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Build the graph
        mp = defaultdict(list)
        N = len(original)
        for i in range(N):
            mp[original[i]].append((changed[i], cost[i]))

        def dijkstra(start: str, end: str) -> int:
            # Min-heap priority queue
            pq = [(0, start)]
            seen = set()

            while pq:
                current_cost, node = heapq.heappop(pq)
                if node in seen:
                    continue
                seen.add(node)
                if node == end:
                    return current_cost

                for neighbor, weight in mp[node]:
                    if neighbor not in seen:
                        heapq.heappush(pq, (current_cost + weight, neighbor))

            return float('inf')  # Return infinity if there's no valid transformation path

        total_cost = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            cost = dijkstra(source[i], target[i])
            if cost == float('inf'):
                return -1
            total_cost += cost

        return total_cost