class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        nums.sort()
        c = 0
        mg = 0
        for i in range(0,n-1):
            gap = abs(nums[i] - nums[i+1])
            if mg < gap:
                mg = gap
        return mg