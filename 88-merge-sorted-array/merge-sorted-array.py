class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curr1 = m-1
        curr2 = n-1
        right = m+n-1

        while curr2 >=0:
            if curr1 >=0 and nums1[curr1] > nums2[curr2]:
                nums1[right] = nums1[curr1]
                curr1 -= 1
            else:
                nums1[right] = nums2[curr2]
                curr2 -= 1
            right -= 1



        