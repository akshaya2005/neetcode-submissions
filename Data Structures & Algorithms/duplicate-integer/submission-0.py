class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurrences = defaultdict(int)
        for i in range(len(nums)):
            occurrences[nums[i]] += 1
            if occurrences[nums[i]] > 1:
                return True
        return False
        