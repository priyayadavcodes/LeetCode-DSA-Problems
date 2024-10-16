class Solution:
    def canPartition(self, arr):
        # Calculate the total sum of the array
        total_sum = sum(arr)

        # If the total sum is odd, it's not possible to partition into two equal subsets
        if total_sum % 2 != 0:
            return False

        # Target sum for each subset
        target_sum = total_sum // 2

        # Create a DP array to store whether a subset with a specific sum can be formed
        dp = [False] * (target_sum + 1)
        dp[0] = True  # A subset with sum 0 is always possible (the empty set)

        # Update the DP array
        for num in arr:
            # Traverse the dp array from right to left to avoid using the same element twice
            for i in range(target_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        # The answer is whether a subset with sum equal to target_sum is possible
        return dp[target_sum]
