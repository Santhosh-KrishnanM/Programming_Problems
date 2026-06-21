class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1, l2 = nums[:n], nums[n:]
        res = []
        for i in range(n):
            res.append(l1[i])
            res.append(l2[i])
        return res