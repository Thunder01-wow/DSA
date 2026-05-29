class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            total = 0
            num = nums[i]
            while num > 0:
                total += num % 10
                num //= 10
            nums[i] = total
        
        return min(nums)

                    