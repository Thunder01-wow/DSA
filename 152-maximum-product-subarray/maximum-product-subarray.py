class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curmax=1
        curmin=1

        for i in nums:
            if i==0:
                curmax=1
                curmin=1
            temp=i * curmax
            curmax=max(i * curmax,i * curmin, i)
            curmin=min(temp ,i * curmin, i)
            res=max(res,curmax)
        return res

        