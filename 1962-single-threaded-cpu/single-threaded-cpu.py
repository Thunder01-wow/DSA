class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i , t in enumerate(tasks):
            t.append(i)
        
        def get(t):
            return t[0]

        tasks.sort(key = get)

        res , Minheap = [] , []
        i , time = 0 , tasks[0][0]

        while Minheap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(Minheap , [ tasks[i][1] , tasks[i][2] ] )
                i += 1

            if Minheap:
                proTime , ind = heapq.heappop(Minheap)
                time += proTime
                res.append(ind)
            else:
                time = tasks[i][0]

        return res