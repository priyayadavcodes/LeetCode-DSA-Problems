class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        n = len(haystack)
        
        if needle in haystack:
            idx = haystack.index(needle)
            return idx
        else:
            return -1

        
        



        