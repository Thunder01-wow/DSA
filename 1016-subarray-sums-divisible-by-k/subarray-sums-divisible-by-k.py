class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = { 0 : 1}
        res = 0
        pre_sum = 0

        for n in nums:
            pre_sum += n
            remain = pre_sum % k

            if remain in count:
                res += count[remain]
            count[remain] = 1 + count.get(remain , 0)

        return res