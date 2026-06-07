class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        Last_idx = {}
        res = []

        for i , v in enumerate(s):
            Last_idx[v] = i
        
        size , end = 0 , 0
        for i , v in enumerate(s):
            size += 1
            if Last_idx[v] > end:
                end = Last_idx[v]

            if i == end:
                res.append(size)
                size = 0
            
        return res