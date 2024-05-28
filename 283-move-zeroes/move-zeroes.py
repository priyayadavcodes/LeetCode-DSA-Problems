class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
           
                nums.append(nums[i])
                nums.remove(nums[i])
            

        