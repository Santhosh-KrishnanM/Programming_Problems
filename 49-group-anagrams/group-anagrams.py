class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for x in strs:
            k = "".join(sorted(x))
            if k not in d:
                d[k] = []
            d[k].append(x)
        return list(d.values())