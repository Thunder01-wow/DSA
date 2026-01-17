class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count={}
        res=0
        heap=[]
        for i in arr:
            count[i] = 1+count.get(i,0)
        
        for n in count.values():
            heapq.heappush(heap,-n)
        val=0
        while len(arr) - val > len(arr)/2:
            val += -1 * heapq.heappop(heap)
            res+=1
        return res
        

        