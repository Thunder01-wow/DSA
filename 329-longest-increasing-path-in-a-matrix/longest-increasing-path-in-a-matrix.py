class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = {}

        def dfs(r , c , prev_val):
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev_val:
                return 0
            
            if (r , c) in res:
                return res[(r,c)]
            
            lip = 1

            lip = max (lip , 1 + dfs(r + 1 , c , matrix[r][c]))
            lip = max (lip , 1 + dfs(r - 1 , c , matrix[r][c]))
            lip = max (lip , 1 + dfs(r , c + 1, matrix[r][c]))
            lip = max (lip , 1 + dfs(r , c - 1 , matrix[r][c]))
            
            res[(r , c )] = lip
            return lip
        
        for r in range(rows):
            for c in range(cols):
                dfs(r , c , -1)

        return max(res.values())