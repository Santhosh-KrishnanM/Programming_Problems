class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)
        d = dict()
        if sl != tl:
            return False
        for i in range(sl):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            else:
                if t[i] in d.values():  
                    return False
                d[s[i]] = t[i]
        return True