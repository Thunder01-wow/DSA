class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res=[]
        l,r=0,len(arr)-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==x:
                start=mid-1
                end=mid+1
                k-=1
                break
            elif arr[mid] > x:
                r=mid-1
            else:
                l=mid+1
        
        if l > r:
            start=r
            end=l
        
        while k:
            if start == -1:
                end+=1
            elif end == len(arr):
                start-=1
            else:
                if abs(arr[start]-x) <= abs(arr[end] -x):
                    start-=1
                else:
                    end+=1
            k-=1
        return arr[start+1:end]