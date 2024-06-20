class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        
        dq = deque()  
        maxvalue = float("-inf")
        
        for x, y in points:
            while dq and x - dq[0][1] > k:
                dq.popleft()

            if dq:
                maxvalue = max(maxvalue, y + x + dq[0][0])

            while dq and y - x >= dq[-1][0]:
                dq.pop()
            
            dq.append((y - x, x))
        
        return maxvalue
