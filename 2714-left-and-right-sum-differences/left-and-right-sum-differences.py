class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = 0 
        suffix = sum(nums)
        res = []

        for i in nums:
            prefix += i
            res.append(abs(prefix - suffix))
            suffix -= i
        
        return res