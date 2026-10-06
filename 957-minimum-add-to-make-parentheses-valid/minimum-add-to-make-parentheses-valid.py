class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c,r = 0,0
        for i in s:
            if i == "(":
                c += 1
            else:
                if c > 0:
                    c -= 1
                else:
                    r += 1
        return r + c