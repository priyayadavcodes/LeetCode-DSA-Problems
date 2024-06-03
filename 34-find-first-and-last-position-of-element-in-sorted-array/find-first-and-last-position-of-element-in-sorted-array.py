class Solution:


    def first_occurrence(self,arr, n, k):
        low = 0
        high = n - 1
        result = -1  
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == k:
                result = mid
                high = mid - 1 
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return result

    def last_occurrence(self,arr, n, k):
        low = 0
        high = n - 1
        result = -1  
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == k:
                result = mid
                low = mid + 1  
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return result

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        k = target
        first = self.first_occurrence(nums,n,k)
        last = self.last_occurrence(nums,n,k)
        return [first,last]
    
        