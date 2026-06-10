class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        maxI = height[0]
        j = len(height) - 1
        maxJ = height[-1]
        water = 0
        while i <= j:
            if maxI < maxJ:
                maxI = max(maxI, height[i])
                water += (maxI - height[i])
                i += 1
            else:
                maxJ = max(maxJ, height[j])
                water += (maxJ - height[j])
                j -= 1
        return water

        