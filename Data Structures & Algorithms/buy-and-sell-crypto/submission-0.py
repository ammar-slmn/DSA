class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buy
        r = 1 # sell
        maxP = 0

        while r < len(prices): 
            #profitable? 
            if prices[l] < prices[r]: 
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: 
                l +=1
            r +=1
        return maxP