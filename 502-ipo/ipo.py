class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        Maxheap = []
        Minheap = [ (c,p) for c,p in zip(capital , profits) ]
        heapq.heapify(Minheap)

        for i in range(k):
            while Minheap and Minheap[0][0] <= w:
                c , p = heapq.heappop(Minheap)
                heapq.heappush(Maxheap, -1 * p)
            if not Maxheap:
                break
            w += -1 * heapq.heappop(Maxheap)
        return w