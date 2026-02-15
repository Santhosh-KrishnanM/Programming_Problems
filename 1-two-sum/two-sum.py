class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ch = {}
        for i,n  in enumerate(nums):
            comp = target - n
            if comp in ch:
                return [ch[comp],i]
            ch[n] = i

s = Solution()
s.twoSum([2,7,11,15],9)