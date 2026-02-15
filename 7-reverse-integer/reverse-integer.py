class Solution:
    def reverse(self, x: int) -> int:
        rem, rev = 0, 0
        neg = x < 0
        x = abs(x)
        while(x > 0):
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10
        if rev < -2147483648 or rev > 2147483647:
            return 0
        return -rev if neg else rev