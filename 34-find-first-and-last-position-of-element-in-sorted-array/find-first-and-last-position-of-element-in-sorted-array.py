class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]        
        first = nums.index(target)        
        last = first
        for i in range(len(nums) - 1, first, -1):
            if nums[i] == target:
                last = i
                break              
        return [first, last]