class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        a = 0
        n = len(candidates)
        def func(x, target, path):
            if target == 0:
                res.append(path)
                return
            if target < 0:
                return
            for i in range(x, n):
                func(i, target - candidates[i], path + [candidates[i]])
        func(0, target, [])
        return res