class Solution:
    def isValid(self,s: str) -> bool:
        ls = []
        paren = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for element in s:
            if len(ls) == 0:
                ls.append(element)
                continue
            if element in paren:
                if ls[-1] == paren[element]:
                    ls.pop()
                    continue
                
            ls.append(element)
        if len(ls) == 0:
            return True
        else:
            return False
            
    