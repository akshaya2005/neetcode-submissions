class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        ## look for the min from the left and look for the max on the right
        i = 0 
        j = 1
        while j < len(prices):
            print(i, j)
            prof = prices[j] - prices[i]
            print(prof)
            maxProf = max(prof, maxProf)
            if prof < 0:
                i = j
                j = i + 1
            else:
                j += 1
        return maxProf

            
            
        