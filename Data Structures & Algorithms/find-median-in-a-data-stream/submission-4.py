class MedianFinder:
    def __init__(self):
        self.nums = []
        self.size = 0

    def addNum(self, num: int) -> None:
        i = 0
        j = len(self.nums) - 1
        
        while i <= j:
            mid = (i + j) // 2
            if self.nums[mid] == num:
                i = mid
                break
            if self.nums[mid] > num:
                j = mid - 1
            else:
                i = mid + 1

        self.nums.insert(i, num)
        self.size += 1

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            median = (self.nums[self.size // 2 - 1] + self.nums[self.size // 2]) / 2
        else:
            median = self.nums[self.size // 2]
        return median
                    
