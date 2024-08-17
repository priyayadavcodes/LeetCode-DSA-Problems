class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area with the current pair of lines
            width = right - left
            min_height = min(height[left], height[right])
            current_area = min_height * width
            
            # Update the maximum area found
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
