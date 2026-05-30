class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        res = float("inf")
        q = deque()

        for r in range(len(nums)):
            curr_sum += nums[r]
            if curr_sum >= k:
                res = min(res , r + 1 )

            while q and curr_sum - q[0][0] >= k:
                prefix , end_inx = q.popleft()
                res = min(res , r - end_inx)

            while q and curr_sum < q[-1][0]:
                q.pop()
            
            q.append((curr_sum , r))
        
        return -1 if res == float("inf") else res
