class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s:
            return 0
        c = s.count(letter)
        return int((c / len(s)) * 100)