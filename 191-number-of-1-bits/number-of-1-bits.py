class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return "0"
        l = []
        c = 0
        while n > 0:
            r = n % 2
            if r == 1:
                c += 1
            l.append(str(r))
            n //= 2
        s = "".join(l)
        print(s)
        return c