class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        res=[]

        for i in nums:
            count[i] = 1+count.get(i,0)

            if len(count) > 2:
                new_count ={}
                for n,c in count.items():
                    if c >1:
                        new_count[n] = c-1
                count=new_count

        for n in count:
            if nums.count(n) > len(nums)//3:
                res.append(n)
        return res

                    
