class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = max(prices)
        sell = 0
        res = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] - buy > res:
                res = prices[i] - buy
        return res