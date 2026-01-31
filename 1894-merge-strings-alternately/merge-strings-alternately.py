class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        L1,L2=0,0

        while L1 < len(word1) and L2 < len(word2):
            res.append(word1[L1])
            res.append(word2[L2])
            L1+=1
            L2+=1
        res.append(word1[L1:])
        res.append(word2[L2:])
        
        return "".join(res)



        