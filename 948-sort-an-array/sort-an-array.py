class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res=[]
        heapq.heapify(nums)
        while nums:
            val=heapq.heappop(nums)
            res.append(val)
        
        return res

            

        