class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            ## pop anything with greater height from the stack
            ## the stack is only ever holding increasing elements
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                
                # so this is a valid height calculation
                maxArea = max(maxArea, height * (i - index))
                start = index
            
            stack.append((start,h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea
        



        

        