class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = 1
        maxP = 0
        while (r < n):
            ## if the price at the left pointer is less 
            ## than the proce at the right pointer
            ## profit = right - left
            ## check and update maxProfit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            ## if profit becomes negative skip past all the positive 
            ## profit numbers
            else:
                l = r
            ## grow the window as long as profit is positive
            r += 1
        return maxP
            
