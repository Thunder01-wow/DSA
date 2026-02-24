class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        seen = set()
        for i in count.values():
            if i in seen:
                return False
            seen.add(i)
        return True