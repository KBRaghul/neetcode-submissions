class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        right, left = 1, 0
        while right < len(prices):
            profit = 0
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            
            right += 1

        return max_profit
