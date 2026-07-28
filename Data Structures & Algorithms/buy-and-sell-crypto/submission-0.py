class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = prices[0]
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if (prices[i] - minPrice) > profit:
                profit = prices[i] - minPrice
        return profit