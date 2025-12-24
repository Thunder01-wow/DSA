class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        comman=set(nums1)
        res=[]
        for i in nums2:
            if i in comman:
                res.append(i)
                comman.remove(i)
        return res