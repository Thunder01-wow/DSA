class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
            rows , cols = len(heights) , len(heights[0])

            minHeap = [[0,0,0]]
            visited = set()
            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            while minHeap:
                diff , r ,c = heapq.heappop(minHeap)
                
                if (r,c) in visited:
                    continue
                visited.add((r,c))
                if (r,c) == (rows - 1 , cols - 1):
                    return diff
                
                for dr , dc in directions:
                    newr , newc = r + dr , c + dc
                    if (newr < 0 or newc < 0 or newr == rows or newc == cols or (newr,newc) in visited):
                        continue
                    newdiff = max(diff,abs(heights[r][c] - heights[newr][newc]))
                    heapq.heappush(minHeap,[newdiff,newr,newc])
