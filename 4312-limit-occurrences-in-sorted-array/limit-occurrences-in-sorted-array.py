class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        l = []
        for i in nums:
            if i not in l:
                if nums.count(i) > k:
                    l1 = [i for _ in range(k)]
                    l.extend(l1)
                else:
                    l2 = [i for _ in range(nums.count(i))]
                    l.extend(l2)
        return l