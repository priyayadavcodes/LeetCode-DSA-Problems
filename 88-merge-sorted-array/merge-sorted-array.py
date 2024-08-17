class Solution:
    def merge(self, arr1: List[int], n: int, arr2: List[int], m: int) -> None:
        i, j = n - 1, m - 1
    
        k = n + m - 1

        while i >= 0 and j >= 0:
            if arr1[i] > arr2[j]:
                arr1[k] = arr1[i]
                i -= 1
            else:
                arr1[k] = arr2[j]
                j -= 1
            k -= 1
        

        while j >= 0:
            arr1[k] = arr2[j]
            j -= 1
            k -= 1
