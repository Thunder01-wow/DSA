class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)):
            new_dp = set()
            for n in dp:
                if (n + nums[i]) == target:
                    return True
                new_dp.add(n + nums[i])
                new_dp.add(n)
            dp = new_dp

        return True if target in dp else False