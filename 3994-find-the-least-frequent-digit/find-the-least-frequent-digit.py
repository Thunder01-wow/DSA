class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        count = Counter(str(n))
        ans = min(count.values())
        res = 10
        for i in count:
            if count[i] == ans:
                res = min(res,int(i))

        return res
