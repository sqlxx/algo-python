class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        buyPrice = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            else:
                if prices[i]- buyPrice > profit:
                    profit = prices[i] - buyPrice

        return profit
