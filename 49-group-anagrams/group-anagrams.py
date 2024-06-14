from collections import Counter
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold grouped anagrams
        anagram_dict = {}

        # Iterate over each string in the list
        for s in strs:
            # Create a sorted tuple of the string as a key
            key = tuple(sorted(s))
            
            # Use Counter for the key if needed:
            # key = tuple(sorted(Counter(s).elements()))
            
            # If the key is not in the dictionary, initialize it with an empty list
            if key not in anagram_dict:
                anagram_dict[key] = []
            
            # Append the current string to the list corresponding to the sorted tuple key
            anagram_dict[key].append(s)
        
        # Return the values of the dictionary as a list of lists
        return list(anagram_dict.values())

