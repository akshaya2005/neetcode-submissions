from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        

        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        
        for num, freq in mp.items():
            buckets[freq].append(num)
        res = []

        print(buckets)
        while len(res) < k:
            if not buckets[-1]:
                buckets.pop()
            else:
                res.append(buckets[-1].pop())
        
        return res



            
            
            