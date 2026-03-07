class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows , cols = len(board) , len(board[0])

        def capture(r,c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return 

            board[r][c] = "T"

            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        
        for r in range(rows):
            capture(r,0)
            capture(r,cols-1)

        for c in range(cols):
            capture(0,c)
            capture(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        