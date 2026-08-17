class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        tot = nums[0]
        j = 1
        while j < len(nums) and nums[j] == nums[j-1] + 1:
            tot += nums[j]
            j += 1
        while True:
            if tot not in nums:
                return tot
            tot += 1
            