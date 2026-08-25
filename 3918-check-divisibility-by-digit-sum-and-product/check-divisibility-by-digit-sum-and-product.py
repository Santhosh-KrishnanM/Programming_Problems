class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        def spDig(n):
            nonlocal s,p
            while n != 0:
                r = n % 10
                s += r
                p *= r
                n //= 10
        spDig(n)
        print(s,p)
        k = s + p
        return True if n % k == 0 else False