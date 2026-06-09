class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: # i am in the left sorted portion if the array
                ## what are the two cases where I want to go right
                if target > nums[mid] or nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                ## two cases where I would want to go left
                if target < nums[mid] or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1


        return -1
                
        