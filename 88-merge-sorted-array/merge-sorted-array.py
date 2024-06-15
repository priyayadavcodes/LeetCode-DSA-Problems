from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Initialize pointers for nums1, nums2, and the end of the merged array
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # Merge the arrays starting from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them over
        nums1[:p2 + 1] = nums2[:p2 + 1]

