class Solution:
    def countKeyChanges(self, s: str) -> int:
        ns = s.lower()
        k = 0
        for i in range(len(ns)-1):
            if(ns[i] != ns[i+1]):
                k += 1
        return k