class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
            else:
                left = right
                            
            if profit > maxProfit:
                maxProfit = profit
            
            right = right + 1

        return maxProfit