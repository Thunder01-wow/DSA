class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) // k
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse = True)
        used = [False] * len(nums)

        def backtrack(i,k,SubsetSum):
            if k == 0:
                return True

            if SubsetSum == target:
                return backtrack(0,k-1,0)
            
            for j in range(i,len(nums)):
                if used[j] or SubsetSum + nums[j] > target:
                    continue
                used[j] = True

                if backtrack(j+1,k,SubsetSum + nums[j]):
                    return True
                
                used[j] = False
                if SubsetSum == 0:
                    break

            return False
        
        return backtrack(0,k,0)