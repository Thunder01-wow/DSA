class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows , cols = len(heights) , len(heights[0])
        pacific , atlantic = set() , set()
        res=[]

        def dfs(r,c,visited,prevHeight):
            if ((r,c) in visited or c < 0 or r < 0 
            or r == rows or c == cols or heights[r][c] < prevHeight):
                return
            
            visited.add((r,c))
            dfs(r + 1 , c , visited , heights[r][c])
            dfs(r - 1, c , visited , heights[r][c])
            dfs(r , c + 1 , visited , heights[r][c])
            dfs(r , c - 1, visited , heights[r][c])


        for r in range(rows):
            dfs(r , 0 , pacific , heights[r][0])
            dfs(r , cols - 1 , atlantic ,heights[r][cols-1])

        for c in range(cols):
            dfs(0 , c , pacific , heights[0][c])
            dfs(rows - 1 , c , atlantic , heights[rows-1][c])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])

        return res
