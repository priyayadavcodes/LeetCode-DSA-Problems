class Solution:
    def reverseVowels(self, s: str) -> str:
        ls = 'aeiouAEIOU'
        vow = []
        for i,char in enumerate(s):
            if char in ls:
                vow.append(char)
                s = s[:i]+'_'+s[i+1:]
        for i,char in enumerate(s):
            if char == '_' and len(vow) > 0:
                s = s[:i]+vow[-1]+s[i+1:]
                vow.pop()       
        return s 


        