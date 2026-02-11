class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l , r = max(weights) , sum(weights)
        res = r

        def currsap(mid: int):
            ships , currcap = 1 , mid
            for i in weights:
                if currcap - i < 0:
                    ships += 1
                    currcap = mid
                currcap -= i
            return ships <= days

        
        while l <= r:
            mid = (l + r)//2
            if currsap(mid):
                res = min(res , mid)
                r = mid - 1
            else:
                l = mid + 1
        return res