class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        alice, bob = 0, 0
        for i in nums:
            if i < 10:
                alice += i
            else:
                bob += i
        return alice != bob