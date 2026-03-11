class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        seen = set(count.values())

        return (len(seen) == 1)