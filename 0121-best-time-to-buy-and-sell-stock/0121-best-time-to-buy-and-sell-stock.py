class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left is buy, right is sell
        maxProfit = 0
        
        while r < len(prices): # r is on day 1
            if prices[l] < prices[r]: # l is 0 so true
                profit = prices[r] - prices[l] # 7 - 0
                maxProfit = max(maxProfit, profit) # 0 = max of 0, 7
            else: # first pass skips
                l = r # l is on day 1 now
            r += 1 # r is now 2
            
        return maxProfit # so on until r is out of bounds to right of len
    

#  [7, 1, 5, 3, 6, 4] we want to buy on day 2 sell on day 5
# len is 6