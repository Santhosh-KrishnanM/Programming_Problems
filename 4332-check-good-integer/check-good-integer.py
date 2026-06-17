class Solution:
    def digitsum(self, n: int):
        r = 0
        while n > 0:
            r += n % 10
            n //= 10
        return r
    
    def squaresum(self, n:int):
        r = 0
        while n > 0:
            r += (n % 10)**2
            n //= 10
        return r

    def checkGoodInteger(self, n: int) -> bool:
        dgsum = self.digitsum(n)
        sqsum = self.squaresum(n)
        x = True if sqsum - dgsum >= 50 else False
        return x