from queue import Queue
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for j in range(m)] for i in range(n)]
        queue = Queue()
        
        # Add all initially rotten oranges to the queue
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.put(((i, j), 0))
                    vis[i][j] = 2
        
        t = 0
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        
        while not queue.empty():
            (r, c), t = queue.get()
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] != 2 and grid[nrow][ncol] == 1:
                    queue.put(((nrow, ncol), t + 1))
                    vis[nrow][ncol] = 2
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] != 2:
                    return -1
        
        return t
