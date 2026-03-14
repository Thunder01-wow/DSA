class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i , eq in enumerate(equations):
            a , b = eq
            adj[a].append([b , values[i]])
            adj[b].append([a , 1 / values[i]])

        def bfs(src,target):
            if src not in adj or target not in adj:
                return -1
            
            visited , q = set() , deque()
            q.append([src , 1])
            visited.add(src)
            while q:
                node , weight = q.popleft()
                if node == target:
                    return weight
                
                for neighbor , w in adj[node]:
                    if neighbor not in visited:
                        q.append([neighbor, w * weight])
                        visited.add(neighbor)
            return -1
        
        res = []
        for q in queries:
            res.append(bfs(q[0] , q[1]))
        
        return res
            


        
