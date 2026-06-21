class Solution:
    def numberOfMatches(self, n: int) -> int:
        a = 0
        while n > 1:
            x = n // 2
            b = n - x
            a += x
            n = b
        return a