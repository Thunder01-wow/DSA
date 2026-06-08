class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l1 , l2 = [] , []
        count = 0

        for n in nums:
            if n < pivot:
                l1.append(n)
            elif n > pivot:
                l2.append(n)
            else:
                count += 1
        
        while count:
            l1.append(pivot)
            count -= 1
        
        return l1 + l2

        