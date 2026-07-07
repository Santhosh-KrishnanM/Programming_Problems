class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        for i in range(c):
            x = matrix[0][i]
            for j in range(r):
                if matrix[j][i] > x:
                    x = matrix[j][i]
            for j in range(r):
                if matrix[j][i] == -1:
                    matrix[j][i] = x
        return matrix