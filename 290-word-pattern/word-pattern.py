class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a = s.split(" ")
        if len(pattern) != len(a):
            return False
        x, y = set(a), set(pattern)
        print(f"{x}  {y}")
        return True if len(x) == len(y) == len(set(zip(pattern, a))) else False