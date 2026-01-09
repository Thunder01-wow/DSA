class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res=[]
        maxHeap=[]
        count=Counter(words)

        for key,val in count.items():
            heapq.heappush(maxHeap,[-val,key])
        
        while k >0:
            val,key=heapq.heappop(maxHeap)
            res.append(key)
            k-=1

        return res