class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                zero = nums[i]
                nums.append(zero)
                nums.remove(zero)
            

        