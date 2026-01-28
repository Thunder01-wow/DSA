class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq=Counter(arr)
        heap=list(freq.values())
        heapq.heapify(heap)
        res=len(heap)

        while k > 0 and heap:
            val=heapq.heappop(heap)
            if k >=val:
                k-=val
                res-=1
        return res
