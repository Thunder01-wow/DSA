class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l , r = max(nums) , sum(nums)
        res = r

        def split(mid: int):
            subarr = 0
            currsum = 0
            for i in nums:
                currsum += i
                if currsum > mid:
                    subarr += 1
                    currsum = i

            return subarr + 1 <= k

        while l <= r:
            mid = l + ((r - l)//2)
            if split(mid):
                res = mid
                r = mid -1
            else:
                l = mid +1
        return res
