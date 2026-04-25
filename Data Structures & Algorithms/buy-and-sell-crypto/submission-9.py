class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: 
            return 0

        l = 0 
        r = 1 
        maxProfit = 0 

        while r < len(prices): 
            if prices[r] > prices[l]: 
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit) 
            else: 
                l = r 
            r += 1
        return maxProfit

            