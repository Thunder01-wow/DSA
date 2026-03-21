class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = { i : [] for i in range(len(points))} # i : [cost , node]

        for i in range(len(points)):
            x1 , y1 = points[i]
            for j in range(i+1,len(points)):
                x2 , y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        #Prim's 
        res = 0
        visited = set()
        minHeap = [[0,0]] #[cost , point]
        while len(visited) < len(points):
            cost , point = heapq.heappop(minHeap)
            if point in visited:
                continue
            res += cost
            visited.add(point)
            for neicost , nei in adj[point]:
                if nei not in visited:
                    heapq.heappush(minHeap,[neicost,nei])
        return res

                 