class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        visited = set()
        minHeap = [[grid[0][0],0,0]]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while minHeap:
            t , r , c = heapq.heappop(minHeap)
            visited.add((r,c))

            if r == rows - 1 and c == cols - 1:
                return t

            for dr , dc in directions:
                newr , newc = r + dr , c + dc 
                if newr < 0 or newc < 0 or newr == rows or newc == cols or (newr,newc) in visited:
                    continue
                visited.add((newr,newc))
                heapq.heappush(minHeap,[max(t , grid[newr][newc]), newr, newc])
        