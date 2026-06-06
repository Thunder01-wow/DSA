class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n , 0)

        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            n = minHeap[0]

            for i in range(n , n + k):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        
        return True