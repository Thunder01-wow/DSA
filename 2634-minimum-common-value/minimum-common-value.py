class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        res = float("inf")
        l , r = 0 , 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                l += 1
            elif nums1[l] > nums2[r]:
                r += 1
            else:
                res = min(res , nums1[l])
                l += 1
                r += 1

        if res == float("inf"):
            return -1
        else:
            return res