class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ## store indices in the deque
        ## monotonically decreasing queue
        window = deque()
      
        res = []

        l = r = 0
        for r in range(len(nums)):
            ## if something is no longer in the window remove it
            

            while window and nums[window[-1]] < nums[r]:
                window.pop()
            
            window.append(r)

            if window[0] < l:
                window.popleft()

            
        
            if ((r + 1) >= k):
                res.append(nums[window[0]])
                l += 1  
        
        return res