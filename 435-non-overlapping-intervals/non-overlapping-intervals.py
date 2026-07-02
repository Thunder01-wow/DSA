class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        Prev_end = intervals[0][1]
        res = 0

        for start , end in intervals[1:]:
            if start >= Prev_end:
                Prev_end = end
            else:
                res += 1
                Prev_end = min(Prev_end , end)

        return res