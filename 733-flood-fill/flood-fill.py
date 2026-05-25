class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        
        def dfs(r , c , sr_color):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] == color or image[r][c] != sr_color:
                return None
            
            image[r][c] = color 

            dfs(r - 1 , c , sr_color)
            dfs(r + 1 , c , sr_color)
            dfs(r , c + 1, sr_color)
            dfs(r , c - 1 , sr_color)

        dfs(sr , sc , image[sr][sc] )
    
        return image
