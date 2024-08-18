class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                nums[k] = nums[i]
                k = k+1
        nums[k] = nums[-1]
        return k+1