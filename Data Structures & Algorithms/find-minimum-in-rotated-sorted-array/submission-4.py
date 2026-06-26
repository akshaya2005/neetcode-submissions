class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## left sorted half and right sorted half

        l = 0
        r = len(nums) - 1
    
        while l <= r:
            
            mid = (l + r) // 2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                if nums[mid - 1] > nums[mid]:
                    return nums[mid]
                else:
                    r = mid - 1
        return nums[l]



       



        