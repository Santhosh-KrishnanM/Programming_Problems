class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        s = list()
        for i in patterns:
            if i in word:
                s.append(i)
        return len(s)