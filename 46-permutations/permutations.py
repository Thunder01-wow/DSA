class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        if (len(nums) == 1):
            return [nums[:]]

        for i in range(len(nums)):
            n=nums.pop(0)
            perm=self.permute(nums)

            for p in perm:
                p.append(n)
            res.extend(perm)
            nums.append(n)
            
        return res

