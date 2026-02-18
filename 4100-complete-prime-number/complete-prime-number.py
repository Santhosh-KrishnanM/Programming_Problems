class Solution:
    def completePrime(self, num: int) -> bool:
        # Whole number must be prime
        if not self.isPrime(num):
            return False

        s = str(num)

        # Check prefixes
        for i in range(1, len(s)):
            prefix = int(s[:i])
            if not self.isPrime(prefix):
                return False

        # Check suffixes
        for i in range(1, len(s)):
            suffix = int(s[i:])
            if not self.isPrime(suffix):
                return False

        return True

    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
