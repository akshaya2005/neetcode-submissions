class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) - 1
        maxI = i
        maxJ = j
        maxArea = 0

        while i < j:
            currArea = min(heights[i], heights[j]) * (j - i)
            maxArea = max(currArea, maxArea)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxArea


        