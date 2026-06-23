class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        res = []

        class item:
            def __init__(self, num, index):
                self.num = num
                self.index = index
            
            def __lt__(self, other):
                return self.num < other.num
            
            def __repr__(self):
                return f"Index:{self.index} Num:{self.num}\n"
        
        for i in range(k):
            heapq.heappush(pq, item(-nums[i], i))
    
        l = 0
        for r in range(k, len(nums) + 1):
            top = pq[0]
        
            while pq and pq[0].index <= l:
                heapq.heappop(pq)
            
            res.append(-top.num)
            if r < len(nums):
                heapq.heappush(pq, item(-nums[r], r))
            l += 1
        return res
            



            

        
        






        