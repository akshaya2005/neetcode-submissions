class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        minBuy = prices[0]
        maxProf = 0
        for sell in prices:
            maxProf = max(maxProf, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxProf
        

        