class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i,j = 0, 0
        psum = 0
        min_len = 99999999
        while i < n:
            psum += nums[i]
            while psum >= target:
                min_len = min(min_len,i-j+1)
                psum -= nums[j]
                j += 1
            i += 1
        if min_len == 99999999:
            return 0
        else:
            return min_len