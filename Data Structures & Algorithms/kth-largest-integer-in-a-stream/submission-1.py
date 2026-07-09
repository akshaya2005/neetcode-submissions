class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify_max(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        print(self.heap)
        heapq.heappush_max(self.heap, val)
        store = []
        for i in range(self.k-1):
            store.append(heapq.heappop_max(self.heap))
        
        val = heapq.heappop_max(self.heap)
        store.append(val)
        for elem in store:
            heapq.heappush_max(self.heap, elem)
        return val
        
