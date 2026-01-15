class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum=set(nums)
        longest=0

        for n in setnum:
            if (n-1) not in setnum:
                length=0
                while (n+length) in setnum:
                    length+=1
                longest=max(length,longest)
        return longest

        