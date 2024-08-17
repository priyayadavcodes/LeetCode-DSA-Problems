class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash = {}
        for i in range(n):
            val = target - nums[i]

            if val in hash :
                return [hash[val]+1, i+1]
            hash[nums[i]] = i