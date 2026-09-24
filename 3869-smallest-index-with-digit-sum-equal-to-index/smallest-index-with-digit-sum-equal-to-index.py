class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        #ind = dict()
        for i,j in enumerate(nums):
            x = 0 
            while j > 0:
                x += j % 10
                j //= 10
            if x == i:
                #ind[i] = x
                return i
        return -1
        #s = min(ind, default = None)
        #return ind[s] if s != None else -1
        