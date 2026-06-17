class SubArrayFreqBalance:
    def __init__(self):
        self._c = Counter()
        self._freqs = Counter()
    
    def add(self, elem):
        old_cnt = self._c[elem]
        self._c[elem] += 1
        if old_cnt != 0:
            if self._freqs[old_cnt] == 1:
                self._freqs.pop(old_cnt)
            else:
                self._freqs[old_cnt] -= 1
        self._freqs[old_cnt + 1] += 1
    
    def check(self):
        if len(self._freqs) != 2:
            return False
        return 2 * min(self._freqs) == max(self._freqs)


class Solution:
    def getLength(self, nums: List[int]) -> int:
        result = max(
            sum(1 for _ in it)
            for _, it in groupby(nums)
        )

        n = len(nums)
        for i in range(n):
            if result >= n - i:
                break
            data = SubArrayFreqBalance()
            for j in range(i, n):
                data.add(nums[j])
                if data.check():
                    result = max(result, j - i + 1)
        return result