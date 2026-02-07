class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        def custom_sort(n):
            return (count[n] , -n )

        nums.sort(key=custom_sort) 
        return nums
        