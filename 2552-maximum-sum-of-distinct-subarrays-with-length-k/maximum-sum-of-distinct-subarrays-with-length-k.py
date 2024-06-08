from typing import List

class Solution:
    def maximumSubarraySum(self, Arr: List[int], K: int) -> int:
        N = len(Arr)
        if K > N:
            return 0
        
        maxsum = 0
        current_sum = 0
        i = 0
        elements = {}
        
        for j in range(N):
            if Arr[j] in elements:
                elements[Arr[j]] += 1
            else:
                elements[Arr[j]] = 1
            
            current_sum += Arr[j]
            
            if j - i + 1 == K:
                if len(elements) == K:  # all elements in the window are unique
                    maxsum = max(maxsum, current_sum)
                
                # Slide the window to the right
                current_sum -= Arr[i]
                if elements[Arr[i]] == 1:
                    del elements[Arr[i]]
                else:
                    elements[Arr[i]] -= 1
                i += 1
        
        return maxsum
