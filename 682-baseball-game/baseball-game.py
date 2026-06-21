class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        for i in operations:
            n = len(l)
            if i == 'C':
                l.pop()
            elif i == 'D':                
                a = l[n - 1] * 2
                l.append(a)
            elif i == '+':
                l.append(l[n - 1] + l[n - 2])
            else:
                l.append(int(i))
        return sum(l)