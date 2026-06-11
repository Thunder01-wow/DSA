class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        def expand(l,r):
            while l >= 0 and r < len(s) and s[r] == s[l]:
                l -= 1
                r += 1
            return s[l + 1: r]

        res = ""

        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)

            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
            
        return res