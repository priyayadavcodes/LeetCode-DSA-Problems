from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Check for empty list
        if not strs:
            return ""
        
        # Initialize the prefix with the first string
        prefix = strs[0]
        
        # Iterate over the rest of the strings
        for string in strs[1:]:
            # Reduce the prefix length until it matches the start of the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix