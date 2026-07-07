class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d = 0
        while n > 0:
            r = n % 10
            d += r
            n //= 10
        return d