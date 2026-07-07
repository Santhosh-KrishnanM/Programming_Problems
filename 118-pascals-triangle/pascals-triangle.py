class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return l
        if numRows == 1:
            return [[1]]
        dp = self.generate(numRows - 1)
        prev = dp[-1]
        cur = [1]
        for i in range(1, numRows-1):
            cur.append(prev[i-1] + prev[i])
        cur.append(1)
        dp.append(cur)
        return dp