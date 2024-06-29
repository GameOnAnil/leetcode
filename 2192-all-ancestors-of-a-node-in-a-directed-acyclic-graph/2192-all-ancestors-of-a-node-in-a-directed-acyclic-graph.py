class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = [0] * n
        
        # Build graph and in-degree array
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Topological sort using Kahn's algorithm
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        ancestors = [set() for _ in range(n)]
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Convert sets to sorted lists
        return [sorted(list(ancestor_set)) for ancestor_set in ancestors]
