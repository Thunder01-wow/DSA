class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        def get_first(i):
            return i[1]

        trips.sort(key = get_first)
        MinHeap = []
        currpass = 0

        for j in trips:
            numpass , start , end = j
            while MinHeap and MinHeap[0][0] <= start:
                currpass -= MinHeap[0][1]
                heapq.heappop(MinHeap)

            currpass += numpass
            if currpass > capacity:
                return False
            
            heapq.heappush(MinHeap , [end,numpass])

        return True


