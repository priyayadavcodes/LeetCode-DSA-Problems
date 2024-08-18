class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
                k = k+1
        