import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = (nums1 + nums2)
        median_val = np.median(merged)
        return float(median_val)