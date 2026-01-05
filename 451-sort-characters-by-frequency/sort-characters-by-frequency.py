class Solution:
    def frequencySort(self, s: str) -> str:
        res=""
        count=Counter(s)
        maxHeap=[]

        for key,val in count.items():
            heapq.heappush(maxHeap,[-val,key])
        
        for i in range(len(maxHeap)):
            val,key=heapq.heappop(maxHeap)
            res += -val * key 
        return res

        