class Solution:
    def pascal(self, rowIndex):
        if rowIndex <= 0:
            return [[1]]
        if rowIndex == 1:
            return [[1]]
        dp = self.pascal(rowIndex - 1)
        prev = dp[-1]
        cur = [1]
        for i in range(1, rowIndex-1):
            cur.append(prev[i-1] + prev[i])
        cur.append(1)
        dp.append(cur)
        return dp

    def getRow(self, rowIndex: int) -> List[int]:
        l = self.pascal(rowIndex+1)
        return l[rowIndex]