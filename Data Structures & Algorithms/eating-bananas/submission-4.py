class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        ## start the eating rate at the max pile size and decrease/increase

        maxSpeed = 0
        for pile in piles:
            if pile > maxSpeed:
                maxSpeed = pile
        
        minSpeed = 1
        
        while minSpeed <= maxSpeed:
            speed = (minSpeed + maxSpeed) // 2
            hours = 0
            for pile in piles:
                hours += (math.ceil(pile/speed))
            
            if hours > h:
                minSpeed = speed + 1
            else:
                maxSpeed = speed - 1
        
        return minSpeed




        