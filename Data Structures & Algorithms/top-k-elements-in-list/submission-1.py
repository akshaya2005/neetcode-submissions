class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = defaultdict(int)

        for i in range(len(nums)):
            dic[nums[i]] += 1
        length = max(dic.values())
        print(length)
        array = [[] for _ in range(length+1)]
        for num, count in dic.items():
            array[count].append(num)
        result = []
        while len(result) < k:
            if len(array[-1]) == 0:
                array.pop()
                continue
            result.append(array[-1].pop())

        return result

        