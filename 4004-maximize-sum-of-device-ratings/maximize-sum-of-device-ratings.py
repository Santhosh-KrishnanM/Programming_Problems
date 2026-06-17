class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        if len(units[0]) == 1:
            return sum(unit[0] for unit in units)

        mins = [heapq.nsmallest(2, unit) for unit in units]
        print(mins)
        sum_2nd_mins = sum(min_2 for _, min_2 in mins)
        global_min = min(min_1 for min_1, _ in mins)
        print(f"{sum_2nd_mins} {global_min}")

        ans = 0

        for min_1, min_2 in mins:
            ans = max(ans, sum_2nd_mins - min_2 + global_min)

        return ans
        