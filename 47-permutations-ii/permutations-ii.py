class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        count = Counter(nums)

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in count:
                if count[i] > 0:
                    curr.append(i)
                    count[i] -= 1
                    backtrack()
                    count[i] += 1
                    curr.pop()

        backtrack()
        return res



        