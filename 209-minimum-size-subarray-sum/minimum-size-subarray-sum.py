class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum = 0
        res = float("inf")
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                res = min(r-l+1,res)
                sum -= nums[l]
                l += 1
        if res == float("inf"):
            return 0
        else:
            return res



        
        