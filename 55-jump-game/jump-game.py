class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums)-1
        to_reach = i
        while i > 0:
            i = i-1
            from_reach = nums[i] + i
            if to_reach <= from_reach:
                to_reach = i
        if to_reach == 0:
            return True
        else:
            return False
