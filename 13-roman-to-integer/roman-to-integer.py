class Solution:
    def romanToInt(self, s: str) -> int:

        romandict = {'I' : 1, 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
        ls = list(s)

        n = len(ls)
        val = 0
        i = 0
 
        while i < n-1:

            if romandict[ls[i]] < romandict[ls[i+1]]:
                val = val-romandict[ls[i]]
                i = i+1
            else:
                val = val + romandict[ls[i]]
                i = i+1

        val = val+romandict[ls[n-1]]
        return val