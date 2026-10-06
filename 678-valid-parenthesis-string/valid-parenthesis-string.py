class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0,0
        for i in s:
            if i == "(":
                low += 1
                high += 1
            elif i == ")":
                if low > 0:
                    low -= 1
                high -= 1
            else:
                if low > 0:
                    low -= 1
                high += 1
            if high < 0:
                return False
        return low == 0