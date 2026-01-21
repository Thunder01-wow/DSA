class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap=[]
        res=0
        for i in matrix:
            for j in i:
                heapq.heappush(min_heap,j)
        while k:
            res=heapq.heappop(min_heap)
            k-=1
        return res




        