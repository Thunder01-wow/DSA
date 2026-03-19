class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge = collections.defaultdict(list)

        for u , v , w in times:
            edge[u].append((v,w))

        minHeap = [(0,k)]
        visited = set()
        res = 0

        while minHeap:
            w1 , n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = max(res,w1)

            for n2 , w2 in edge[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap,(w1 + w2 , n2))

        if len(visited) == n:
            return res
        else:
            return -1