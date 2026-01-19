class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap=[]
        k=len(nums)
        left=right=nums[0][0]

        for i in range(k):
            curr=nums[i]
            left=min(left,curr[0])
            right=max(right,curr[0])
            heapq.heappush(min_heap,(curr[0],i,0))
        
        res=[left,right]

        while True:
            curr_val,i,index=heapq.heappop(min_heap)
            index+=1

            if index==len(nums[i]):
                return res
            
            next_val=nums[i][index]
            heapq.heappush(min_heap,(next_val,i,index))

            right=max(right,next_val)
            left=min_heap[0][0]
            if right - left < res[1] - res[0]:
                res=[left,right]
        