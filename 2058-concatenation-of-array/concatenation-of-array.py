class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res=[]
        i=0
        while i < 2*len(nums):
            i=i%len(nums)
            res.append(nums[i])
            if len(res)==2*len(nums):
                break
            i+=1
        return res
        