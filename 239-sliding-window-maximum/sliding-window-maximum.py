from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)
        result = []
        window = []
        
        for i in range(n):
            # Remove elements that are out of the current window
            if window and window[0] < i - k + 1:
                window.pop(0)
            
            # Remove elements from the list which are smaller than the current element
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            # Add the current element index to the list
            window.append(i)
            
            # Append the maximum element of the window to the result list
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result
