class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append((value, timestamp))
       
        
    def insert(value, array):
        l, r = 0, len(array) - 1
        while l <= r:
            mid = (l + r) // 2
            if array[mid] <= value[1]:
                l = mid + 1
            else:
                r = mid - 1
        array.insert(l, value)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        nums = self.keystore.get(key, [])
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m][1] <= timestamp:
                res = nums[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


    
        
