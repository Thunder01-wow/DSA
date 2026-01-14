class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        res=[]
        for i in range (len(nums)):
            if nums[i] % 2==0:
                res.append(nums[i])
        count=Counter(res)
        if not count:
            return -1
        maxx = 0    
        output = -1        
        for num, count in count.items():
            if count > maxx:
                maxx, output = count, num
            elif count == maxx:
                output = min(num,output)
        return output




        