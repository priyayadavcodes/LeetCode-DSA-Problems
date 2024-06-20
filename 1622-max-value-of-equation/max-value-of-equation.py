class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        
        dq = deque()  # to store the points in the form (y - x, x)
        maxvalue = float("-inf")
        
        for x, y in points:
            # Remove points from deque which are out of the window |x1 - x2| > k
            while dq and x - dq[0][1] > k:
                dq.popleft()
            
            # Calculate the maximum value of the equation using the current point and the point in front of the deque
            if dq:
                maxvalue = max(maxvalue, y + x + dq[0][0])
            
            # Maintain the deque in decreasing order of (y - x)
            while dq and y - x >= dq[-1][0]:
                dq.pop()
            
            # Add the current point to the deque
            dq.append((y - x, x))
        
        return maxvalue
