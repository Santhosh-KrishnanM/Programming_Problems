class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        print(len(s),len(nums))
        if len(nums) == len(s):
            return False
        return True