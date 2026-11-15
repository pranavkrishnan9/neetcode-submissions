class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #input = int prices[] where prices[i] indicates price of Neetcoin on ith day
        #output = max profit to buy and sell
        maxProfit = 0
        profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                if profit > maxProfit:
                    maxProfit = profit
            right += 1
        return maxProfit
