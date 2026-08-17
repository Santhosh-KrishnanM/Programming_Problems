from collections import Counter

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = Counter(x % 3 for x in stones)
        print(cnt)

        if cnt[0]%2 == 0:
            print(cnt[0],cnt[1],cnt[2])
            return cnt[1] > 0 and cnt[2] > 0
        
        else:
            return abs(cnt[1]-cnt[2]) > 2
