class Solution:
    def findAnagrams(self, txt: str, pat: str) -> List[int]:
        N = len(txt)
        k = len(pat)
        i, j = 0, 0
        ls = []
    
        unq_ele = set(pat)
        ele_cnts = {element: pat.count(element) for element in unq_ele}
        count = len(ele_cnts)
    
        while j < N:
            if txt[j] in ele_cnts:
                ele_cnts[txt[j]] -= 1
                if ele_cnts[txt[j]] == 0:
                    count -= 1
    
            if j - i + 1 < k:
                j += 1
            else:
                if count == 0:
                    ls.append(j-k+1)
                if txt[i] in ele_cnts:
                    
                    ele_cnts[txt[i]] += 1
                    if ele_cnts[txt[i]] == 1:
                        count += 1
                i += 1
                j += 1
        return ls
        