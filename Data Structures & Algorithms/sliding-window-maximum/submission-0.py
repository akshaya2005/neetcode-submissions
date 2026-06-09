class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = k
        res = []
        mx = float('-inf')
        maxInd = -1
        ## find the max in the first k elements
        for i in range(k):
            if nums[i] > mx:
                mx = nums[i]
                maxInd = i
        
        res.append(mx)
        for l in range(1, len(nums) - k + 1):
            print(l, r)
            print(mx, maxInd)
            
            if l <= maxInd:
                print("if ran")
                if nums[r] > mx:
                    mx = nums[r]
                    maxInd = r
            else:
                print("else ran")
                m = float('-inf')
                for j in range(l, l + k):
                    if nums[j] > m:
                        mi = j
                        m = nums[j]
                mx = m
                maxInd = mi
            
            r += 1
            res.append(mx)
            print()
        
        return res
            
                

        