class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        ls = []
    
        for left in range(n):
            if nums[left] != val:
                nums[k] = nums[left] 
                k = k+1
        return k
    