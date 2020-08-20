class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        total = 0 
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                total += prices[i] - prices[i-1]

        return total 


    def maxProfit2(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        buyPrice = prices[0]
        profit = 0
        total = 0
        sellPrice = -1

        for i in range(1, len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
                total += profit
                profit = 0
            elif prices[i] - buyPrice > profit:
                sellPrice = prices[i]
                profit = sellPrice - buyPrice
            elif prices[i] < sellPrice:
                total += profit
                buyPrice = prices[i]
                sellPrice = -1
                profit = 0

        return total + profit
