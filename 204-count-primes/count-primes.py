class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        
        isPrime = [True] * n
        count = 0
        
        if n > 0:
            isPrime[0] = False
        if n > 1:
            isPrime[1] = False
        
        for i in range(n):
            if isPrime[i]:
                count += 1
                j = i * 2
                while j < n:
                    isPrime[j] = False
                    j += i
        
        return count