class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s=Counter(s)
        count_t=Counter(t)

        for i in count_t:
            if i  not in count_s:
                return i
            if count_s[i]<count_t[i]:
                return i
         
    