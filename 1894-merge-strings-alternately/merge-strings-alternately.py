class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ""
        l = []
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                l.append(word1[i])
            if i < len(word2):
                l.append(word2[i])
            i += 1
        res = "".join(l)
        return res