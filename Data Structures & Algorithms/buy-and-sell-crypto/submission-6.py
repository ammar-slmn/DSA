class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # loop through prices with 2 pointers
        l, r = 0, 1 
        maxProfit = 0 
        while r < len(prices): 
            # check if the right pointer is higher than the left 
            if prices[r] > prices[l]: 
                # if so, find the profit and set the maximum profit
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else: 
                # if not, move the left pointer to the right
                l = r 
            r += 1
        return maxProfit
