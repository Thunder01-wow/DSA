class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        L1,L2=0,0

        while L1 < len(word1) and L2 < len(word2):
            res+=word1[L1]
            L1+=1
            res+=word2[L2]
            L2+=1
        
        while L1 < len(word1):
            res+=word1[L1]
            L1+=1
        
        while L2 < len(word2):
            res+=word2[L2]
            L2+=1
        
        return res



        