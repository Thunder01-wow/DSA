class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        seen = set()
        for i , j in count.items():
            if j == 1:
                seen.add(i)
        return sum(seen)
            


        