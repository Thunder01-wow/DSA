class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max , global_max = 0 , nums[0]
        curr_min , global_min = 0 , nums[0]
        total = 0

        for i in nums:
            curr_max = max(curr_max + i , i)
            curr_min = min(curr_min + i , i)
            total += i

            global_max = max(global_max , curr_max)
            global_min = min(global_min , curr_min)

        if global_max < 0:
            return global_max
        else:
            return max(global_max , total - global_min )