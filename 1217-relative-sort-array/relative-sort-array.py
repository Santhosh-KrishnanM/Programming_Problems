class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res  = []
        count = {}
        for i in arr1:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for num in arr2:
            if num in count:
                res.extend([num]*count[num])
                del count[num]
        for i in sorted(count.keys()):
            res.extend([i]*count[i])
        return res