from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pattern = r'[^\w\s]'
        paragraph = re.sub(pattern, ' ', paragraph)
        paragraph = paragraph.lower()
        para = paragraph.split()
        
        my_dict = Counter(para)
        n = len(banned)
        for i in range(n):
            if banned[i] in my_dict:
                my_dict.pop(banned[i])
  
        max_key = max(my_dict, key=my_dict.get)
        return max_key


        

