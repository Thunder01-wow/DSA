class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap=[]
        val=0
        for i in range(len(nums)):
            heapq.heappush(heap,-1*int(nums[i]))
        while k:
            val= -1 * heapq.heappop(heap)
            k-=1
        return str(val)

        