class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if 1 == nums.count(i):
                return i                