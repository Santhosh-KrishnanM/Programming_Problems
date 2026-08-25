class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        def spDig(n):
            nonlocal s,p
            while n != 0:
                s += n % 10
                p *= n % 10
                n //= 10
        spDig(n)
        k = s + p
        return True if n % k == 0 else False