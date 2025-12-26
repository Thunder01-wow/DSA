class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        l,r=0,0
        q=collections.deque()
        while r < len(nums):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            
            if (r+1) >=k:
                res.append(q[0])
                if nums[l] == q[0]:
                    q.popleft()
                l+=1
            r+=1
        return res
            