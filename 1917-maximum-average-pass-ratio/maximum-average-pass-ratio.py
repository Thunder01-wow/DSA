class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        p,t=0,0
        max_heap=[]
        for i in range(len(classes)):
            p,t=classes[i]
            gain=(p+1)/(t+1) - (p/t)
            heapq.heappush(max_heap,[-1 * gain,i])
        
        while extraStudents:
            gain,i=heapq.heappop(max_heap)
            classes[i][0]+=1
            classes[i][1]+=1
            p,t=classes[i]
            new_gain=(p+1)/(t+1) - (p/t)
            heapq.heappush(max_heap,[-1 * new_gain,i])
            extraStudents -=1

        res=0
        for p,t in classes:
            res+= p/t

        return res/len(classes)
            

        





        