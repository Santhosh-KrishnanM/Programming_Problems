class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        cur = k
        while cur in s:
            cur += k
        return cur