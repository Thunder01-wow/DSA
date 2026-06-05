class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False

    def addword(self , word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isword = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addword(w)

        rows , cols = len(board) , len(board[0])
        visited = set()
        res = set()

        def dfs(r , c , node , word):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r , c) in visited or board[r][c] not in node.children:
                return None
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isword:
                res.add(word)

            dfs(r + 1, c , node , word)
            dfs(r - 1 , c , node , word)
            dfs(r , c + 1, node , word)
            dfs(r , c - 1 , node , word)

            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r , c , root ,"") 

        return list(res)