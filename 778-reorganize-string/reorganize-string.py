class Solution:
    def reorganizeString(self, s: str) -> str:
        res=""
        maxheap=[]
        count=Counter(s)

        for i,j in count.items():
            heapq.heappush(maxheap,(-j,i))

        while maxheap:
            i,j=heapq.heappop(maxheap)
            if len(res) > 0 and res[-1] == j:
                if not maxheap:
                    return ""
                count2,char2=heapq.heappop(maxheap)
                res+=char2
                count2+=1
                if count2:
                    heapq.heappush(maxheap,(count2,char2))
            else:
                res+=j
                i+=1
            if i:
                heapq.heappush(maxheap,(i,j))
        return res


        