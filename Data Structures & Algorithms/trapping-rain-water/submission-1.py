class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = height[0]
        rightMax = height[-1]
        water = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                leftMax = max(leftMax, height[left])
                water += (leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                water += (rightMax - height[right])
        return water
        