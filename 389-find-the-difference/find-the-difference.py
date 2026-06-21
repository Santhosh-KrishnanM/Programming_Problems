class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = dict()
        l = 0
        for i in s:
            l ^= ord(i)
        for j in t:
            l ^= ord(j)
        return chr(l)