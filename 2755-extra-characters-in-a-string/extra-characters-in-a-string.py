class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class Trie:
    def __init__(self,word):
        self.root = TrieNode()
        for w in word:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.endofword = True
        
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary)
        main = trie.root
        cache = {len(s) : 0}

        def dfs(i):
            if i in cache:
                return cache[i]

            res = 1 + dfs(i+1)
            curr = main
            for j in range(i,len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.endofword:
                    res = min(res,dfs(j+1))
            cache[i] = res
            return res 
        
        return dfs(0)