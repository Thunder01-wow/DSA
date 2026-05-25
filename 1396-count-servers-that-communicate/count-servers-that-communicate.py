class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        res = 0
        row_count = [0] * rows
        cols_count = [0] * cols


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    cols_count[c] += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (row_count[r] > 1 or cols_count[c] > 1):
                    res += 1
        
        return res

