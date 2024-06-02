class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        
        
        for i in range(n) :
            if val in nums:
                nums.remove(val)
            
        return len(nums)
        

