class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 1
        if num < 2:
            return False
        for i in range(2,int(num**0.5)+1): 
            if num % i == 0:
                s += i + num // i
        return True if s == num else False