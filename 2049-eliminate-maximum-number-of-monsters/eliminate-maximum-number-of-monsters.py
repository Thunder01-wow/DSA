class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        reach = []
        for d , s in zip(dist , speed):
            minute = math.ceil(d/s)
            reach.append(minute)

        reach.sort()
        res = 0

        for i in range(len(reach)):
            if i >= reach[i]:
                break
            res += 1
        
        return res