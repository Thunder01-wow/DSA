class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n 
        prices[src] = 0

        for i in range(k+1):
            temp = prices.copy()

            for source , dest , cost in (flights):
                if prices[source] == float("inf"):
                    continue
                
                if prices[source] + cost < temp[dest]:
                    temp[dest] = prices[source] + cost
                
            prices = temp

        if prices[dst] == float("inf"):
            return -1
        return prices[dst]