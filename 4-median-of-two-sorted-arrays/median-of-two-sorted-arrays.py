
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge both arrays
        merged = sorted(nums1 + nums2)
        n = len(merged)
        
        # Check if the total length is odd
        if n % 2 == 1:
            # Return the middle element if odd
            return merged[n // 2]
        else:
            # Return the average of the two middle elements if even
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
