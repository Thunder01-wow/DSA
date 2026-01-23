class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res={}
        for i , val in enumerate(nums):
            if val in res and i - res[val] <=k:
                return True
            else:
                res[val]=i
        
        return False
                   