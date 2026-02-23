class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.split())
        d = s.split(" ")
        l = d[::-1]
        return " ".join(l)