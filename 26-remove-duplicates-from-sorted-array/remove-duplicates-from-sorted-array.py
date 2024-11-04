class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        num = nums[n-1]
        k = n
        for i in range(n-1,0,-1):
            a = nums[i-1]
            if a == num:
                nums.pop(i-1)
                nums.append(a)
                k = k-1
            else:
                num = nums[i-1]
        return k