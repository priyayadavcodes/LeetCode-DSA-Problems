class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lsdic = {}
        ls = []
        for i in range(len(list1)):
            if list1[i] in list2:
                idx = list2.index(list1[i])
                lsdic[list1[i]] = i+idx

        
        min_value = min(lsdic.values())
        min_keys = [key for key in lsdic if lsdic[key] == min_value]
        
        return min_keys
