class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## Start by binary searching across the number of bananas you can eat per hour
        l, r = 1, max(piles)
        res = 0 ## final bananas per hour
        while l <= r:
            mid = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/mid)
            if totalTime <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res



        