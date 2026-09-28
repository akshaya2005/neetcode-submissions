class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        maxProf = 0
        i = 0
        while i < len(prices) - 1:
            j = i + 1
            while j < len(prices) and -prices[i] + prices[j] > 0:
                maxProf = max(maxProf, -prices[i] + prices[j])
                j += 1
            i = j
            
        
        return maxProf

        
        

        