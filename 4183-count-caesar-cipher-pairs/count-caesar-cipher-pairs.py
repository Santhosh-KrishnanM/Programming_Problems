class Solution:
    def countPairs(self, words: list[str]) -> int:

        @cache                                          # <-- 1)   
        def wordKey(word: str)-> list:
            dif = ord(word[0])
            return tuple((ord(ch) - dif)%26 for ch in word)


        d, ans = defaultdict(int), 0                    # <-- 2) 
        for word in words:
            d[wordKey(word)]+= 1
            
        return sum(k * k -k for k in d.values())//2     # <-- 3) 