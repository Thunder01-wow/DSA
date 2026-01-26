class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res=[]
        
        for i in range(2*len(nums)):
            res.append(nums[i%len(nums)])

        return res
        