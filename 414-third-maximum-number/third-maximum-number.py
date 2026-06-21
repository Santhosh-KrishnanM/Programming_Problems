class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = b = c = None
        if len(nums) < 3:
            return max(nums)
        for i in nums:
            if i == a or i == b or i == c:
                continue
            if a is None or i > a:
                c,b,a = b, a, i
            elif b is None or i > b:
                c,b = b, i
            elif c is None or i > c:
                c = i
        return c if c is not None else a