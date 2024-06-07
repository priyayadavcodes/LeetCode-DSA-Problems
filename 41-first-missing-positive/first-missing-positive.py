class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # First step is to place each number in its right place
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap elements to their correct positions
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Second step is to find the first place where the index does not match the value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
