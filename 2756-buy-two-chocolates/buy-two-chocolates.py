class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapq.heapify(prices)
        min1 = heapq.heappop(prices)
        min2 = heapq.heappop(prices)

        left = money - (min1 + min2)

        return left if left >= 0 else money
