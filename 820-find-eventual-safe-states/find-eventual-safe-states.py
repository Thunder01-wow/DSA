class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        res = []

        def dfs(i):
            if i in safe:
                return safe[i]

            safe[i] = False
            for edge in graph[i]:
                if not dfs(edge):
                    return safe[i]
                
            safe[i] = True
            return True

        for i in range(n):
            if dfs(i):
                res.append(i)
        return res