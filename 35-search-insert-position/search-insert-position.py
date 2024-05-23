class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        ans = n

        while (low<=high):
            mid = (low+high)//2
        
            if nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
                ans = mid
                
        return ans