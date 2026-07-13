class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ## is this just quickselect?
        def partition(start, end, nums):
            pivotIndex = end
            pivot = nums[pivotIndex]

            ## swap pivot and left
            temp = nums[start]
            nums[start] = nums[pivotIndex]
            nums[pivotIndex] = temp
            i = start + 1
            j = end
            while i <= j:
                while i <= j and nums[i] >= nums[start]:
                    i += 1
                while i <= j and nums[j] <= nums[start]:
                    j -= 1
                
                if i <= j:
                    temp = nums[i] 
                    nums[i] = nums[j]
                    nums[j] = temp
            
            temp = nums[j]
            nums[j] = nums[start]
            nums[start] = temp
        
            if j == k - 1:
                return nums[j]
            
            elif j > k - 1:
                return partition(start, j - 1, nums)
            else:
                return partition(j + 1, end, nums)
        
        return partition(0, len(nums) - 1, nums)
        
        


        