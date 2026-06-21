class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l = list(sentence)
        s = set(l)
        return True if len(s) == 26 else False