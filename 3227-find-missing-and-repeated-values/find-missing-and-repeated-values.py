class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        r = len(grid)
        c = r * r
        l = [0] * (c+1)
        for i in range(r):
            for j in range(r):
                l[grid[i][j]] += 1
        a,b = -1, -1
        for i in range(1,c+1):
            if l[i] == 2:
                a = i
            elif l[i] == 0:
                b = i
        return [a, b]
