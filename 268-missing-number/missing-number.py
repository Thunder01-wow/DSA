class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target=len(nums)*(len(nums)+1)//2
        sum_nums=sum(nums)
        return (target-sum_nums)

        

        