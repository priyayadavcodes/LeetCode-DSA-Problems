class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            if nums[0] == val:
                return 0 
            else:
                return 1
        
        for i in range(n) :
            if val in nums:
                nums.remove(val)
            
        return len(nums)
        

