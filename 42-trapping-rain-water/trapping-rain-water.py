class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l=0
        r=len(height)-1
        rmax=height[r]
        lmax=height[l]
        res=0

        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(lmax,height[l])
                res+=lmax-height[l]
            else:
                r-=1                                
                rmax=max(rmax,height[r])
                res+=rmax-height[r]
        return res

                

        