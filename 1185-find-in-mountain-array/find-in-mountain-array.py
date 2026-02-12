# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        # Find Peak
        l , r = 1 , length - 2
        while l <= r:
            m = (l+r)//2
            left ,mid ,right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m
    
        # Search in left
        l , r = 0 , peak
        while l <= r:
            mid = (l+r)//2
            val = mountainArr.get(mid)
            if val > target:
                r = mid - 1
            elif val < target:
                l = mid + 1
            else:
                return mid

         # Search in right
        l , r = peak , mountainArr.length() - 1
        while l <= r:
            mid = (l+r)//2
            val = mountainArr.get(mid)
            if val > target:
                l = mid + 1
            elif val < target:
                r = mid - 1
            else:
                return mid

        return -1
                

