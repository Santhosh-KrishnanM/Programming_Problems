class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_v = max(candies)
        l = []
        for i in candies:
            s = i + extraCandies
            if s >= max_v:
                l.append(True)
            else:
                l.append(False)
        return l        