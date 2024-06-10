
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        dq = deque()
        result = []
        
        for i in range(len(nums)):
            # Remove indices that are out of the bounds of the sliding window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove elements from the deque which are smaller than the current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Add the current element index to the deque
            dq.append(i)
            
            # Append the maximum element of the window to the result list
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
