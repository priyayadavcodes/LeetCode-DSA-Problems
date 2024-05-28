class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n-1):
            a = s[n-1]
            s.pop()
            s.insert(i,a)
            

