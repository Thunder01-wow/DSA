class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = collections.defaultdict(list)
        degree = [0] * n

        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[v] += 1
            degree[u] += 1

        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
        
        node = n

        while node > 2:
            size = len(q)
            node -= size

            for j in range(size):
                curr = q.popleft()

                for nei in adj[curr]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)

        return list(q)