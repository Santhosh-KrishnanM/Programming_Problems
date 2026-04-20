class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        res = []
        
        def backtrack(curr: list):
            if len(curr) == n:
                res.append(curr[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                
                used[i] = True
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
                used[i] = False
            return
        
        backtrack([])
        return res