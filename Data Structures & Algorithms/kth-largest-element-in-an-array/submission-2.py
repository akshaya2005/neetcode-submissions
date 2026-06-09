class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ## since we are trying to find the largest element and not the smallest
        k = len(nums) - k
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    temp = nums[p]
                    nums[p] = nums[i]
                    nums[i] = temp

                    p += 1
            temp = nums[p]
            nums[p] = nums[r]
            nums[r] = temp
            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1)