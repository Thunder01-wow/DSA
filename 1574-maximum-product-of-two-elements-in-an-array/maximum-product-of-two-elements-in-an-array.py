class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxHeap=[-i for i in nums]
        heapq.heapify(maxHeap)

        i=heapq.heappop(maxHeap)
        j=heapq.heappop(maxHeap)

        return (abs(i) - 1) * (abs(j) - 1)