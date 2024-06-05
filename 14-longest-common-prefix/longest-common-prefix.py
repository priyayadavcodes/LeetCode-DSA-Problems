class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        
        if n == 1 and strs[0] == "":
            return ""
        if n == 1:
            return (''+ strs[0] +'')

        
        lst = []
        for i in range(n-1):
            ls = strs[i]
            m = min(len(strs[i]),len(strs[i+1]))
            count = 0
            if m == 1:
                if strs[i][0] == strs[i+1][0]:
                    lst.append(strs[i][0])
            else:
                
                    
                for j in range(m):
                    a = strs[i][0:j+1]
                    b = strs[i+1][0:j+1]
                    if a == b:
                        lsi = strs[i][0:j+1]
                        count = count+1
                    
                if count>0:
                    lst.append(lsi)
            if len(lst) != i+1:
                return ""

        if len(lst)== 0:
            return ""
            
        else:
            length = 1000
            for i in range(len(lst)):
                ln = len(lst[i])
                if ln < length:
                    length = ln
            v = lst[0][0:length]
            s = str(v)
            return s