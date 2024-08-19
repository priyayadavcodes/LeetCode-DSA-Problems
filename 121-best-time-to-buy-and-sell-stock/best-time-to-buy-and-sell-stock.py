class Solution:
    def maxProfit(self, price: List[int]) -> int:        
        n = len(price)
        left = 0
        right = 1
        min_price = float("inf")
        max_profit = 0

        while right < n:
            curr_price = price[left]
            curr_profit = price[right] - curr_price
            if curr_price < price[right]:
                max_profit = max(max_profit,curr_profit)
            else:
                left = right
            right = right+1
        return max_profit

        return max_profit

# n = len(price)
        # max_profit = 0
        # min_price = float("inf")

        # for j in range(n-1):
        #     curr_price = price[j]
        #     min_price = min(min_price,curr_price)
        #     if curr_price <= min_price:
        #         for i in range(j+1,n):
        #             profit = price[i] - curr_price
        #             max_profit = max(max_profit,profit)
        # return max_profit