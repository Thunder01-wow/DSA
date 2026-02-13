class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1 , nums2
        total = len(nums1) + len(nums2)
        half = total//2

        if len(A) > len(B):
            A , B = B , A

        l , r = 0 , len(A) - 1
        while True:
            mid = (l+r)//2 
            i = half - mid - 2

            if mid >= 0:
                Aleft = A[mid]
            else:
                Aleft = float("-infinity")

            if mid + 1 < len(A):
                Aright = A[mid+1]
            else:
                Aright = float("infinity")

            if i >= 0:
                Bleft = B[i]
            else:
                Bleft = float("-infinity")

            if i + 1 < len(B):
                Bright = B[i+1]
            else:
                Bright = float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright,Bright)
                return ( max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1