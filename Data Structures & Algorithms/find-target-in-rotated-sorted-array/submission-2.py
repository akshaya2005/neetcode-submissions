class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        ## in every iteration mid is either in the left 
        ## sorted half or the right sorted half
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            ## in left sorted half
            if nums[mid] >= nums[left]:
                if nums[left] > target or nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            ## in right sorted half
            else:
                if nums[right] < target or nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

                
