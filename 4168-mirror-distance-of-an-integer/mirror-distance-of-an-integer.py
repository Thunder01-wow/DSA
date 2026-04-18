class Solution:
    def mirrorDistance(self, n: int) -> int:
        if 0 <= n <= 9:
            return 0

        temp = n
        rev = 0
        while n:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10

        return abs(temp - rev) 