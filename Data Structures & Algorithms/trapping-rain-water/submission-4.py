class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        rightMax = height[-1]

        l, r = 0, len(height) - 1
        water = 0

        while l <= r:
            if leftMax <= rightMax:
                ## setting max before subtracting leftMax - height[l]
                ## ensures that the difference is never negative
                leftMax = max(height[l], leftMax)
                water += (leftMax - height[l])
                l += 1
            
            else:
                rightMax = max(rightMax, height[r])
                water += (rightMax - height[r])
                r -= 1
        
        return water
        