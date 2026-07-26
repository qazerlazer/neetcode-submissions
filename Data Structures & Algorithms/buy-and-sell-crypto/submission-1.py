class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        l = len(prices)
        for i in range(0,l):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > profit:
                profit = prices[i] - min
        return profit
        