class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        ans = False
        if n <= 0:
            return ans
        while n%3 == 0:
            n = n//3
        return n==1
        