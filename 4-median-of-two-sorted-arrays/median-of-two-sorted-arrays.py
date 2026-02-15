class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        arr = sorted(nums1)
        n = len(arr)
        res = 0
        mid = n //2
        if n % 2 != 0:
            res = float(arr[mid])
        else:
            res = (arr[mid] + arr[mid - 1]) / 2
        return res