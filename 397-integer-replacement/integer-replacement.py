class Solution:
    def integerReplacement(self, n: int) -> int:
        if n==1:
            return 0
        res=0
        while n>1:
            if n % 2==0:
                n=n//2
            else:
                if n ==3 or n % 4 ==1:
                    n-=1
                else:
                    n+=1
            res+=1
        return res
            


        