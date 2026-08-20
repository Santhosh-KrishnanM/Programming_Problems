class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def productDigit(temp):
            res = 1
            while temp:
                res *= temp % 10
                temp //= 10
            return res
        while productDigit(n) % t != 0:
            n += 1
        return n