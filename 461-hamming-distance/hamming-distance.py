class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c = 0
        if x == y:
            return 0
        while x > 0 or y > 0:
            bx, by = 0, 0
            if x > 0:
                bx = x % 2
                x //= 2
            if y > 0:
                by = y % 2
                y //= 2
            if bx != by:
                c += 1
        return c