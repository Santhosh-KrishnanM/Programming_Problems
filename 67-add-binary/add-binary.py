class Solution:
    def addBinary(self, a: str, b: str) -> str:
        d1, d2 = 0, 0
        for i in a:
            d1 = (d1 * 2) + int(i)
        for j in b:
            d2 = (d2 * 2) + int(j)
        d = d1 + d2
        if d == 0:
            return "0"
        l = []
        while d > 0:
            r = d % 2
            l.append(str(r))
            d //= 2
        return "".join(l)[::-1]