class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        low = 0
        high = n-1
        ans = -1
        

        while low <= high:

            mid = (low+high)//2 
            
            if nums[mid] == target:
                ans = mid
            
            if nums[low] <= nums[mid]:

                if nums[low] <= target and nums[mid] >= target: 
                    high = mid-1
                    
                    
                else:
                    low = mid+1
            
            else:
                if nums[mid]<=target and nums[high]>=target:
                    low = mid+1
                    
                else:
                    high = mid-1
        return ans
                    