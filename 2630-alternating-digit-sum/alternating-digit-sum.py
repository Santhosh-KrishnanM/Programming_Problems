class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = 0
        c = 1 if len(str(n)) % 2 != 0 else -1
        while n != 0:
            res = n % 10
            s += c * res
            c *= -1
            n //= 10
        return s
