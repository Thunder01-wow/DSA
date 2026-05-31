class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = { 0 : -1}
        count , res = 0 , 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            
            if count in hashmap:
                res = max(res , i - hashmap[count])
            else:
                hashmap[count] = i
            
        return res

        
        