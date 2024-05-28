class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n//2):
            a = s[i]
            s[i] = s[n-1-i]
            s[n-1-i] = a
            
            

