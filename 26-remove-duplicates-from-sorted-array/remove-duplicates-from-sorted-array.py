class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        insert_pos = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[insert_pos] = nums[i]
                insert_pos += 1


        unique_count = insert_pos
        return unique_count
                            
