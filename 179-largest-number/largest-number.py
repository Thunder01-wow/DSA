class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i , n in enumerate(nums):
            nums[i] = str(n)

        def largest(n1 , n2):
            if n1 + n2 > n2 + n1:
                return -1
            elif n1 + n2 < n2 + n1:
                return 1
            else:
                return 0

        res = sorted(nums , key = cmp_to_key(largest))

        return str(int("".join(res)))