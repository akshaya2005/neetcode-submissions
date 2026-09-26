class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lot = defaultdict(int)

        for i, char in enumerate(s):
            lot[char] = i
        
        res = []
        size = 0
        end = 0
        for i,c in enumerate(s):
            ## if a character is included in the first partition, 
            ## all of its occurrences must appear in that partition
            ## until you reach the last occurrence, keep increasing
            ## the size of the partition
            size += 1
            end = max(end, lot[c])

            if i == end:
                res.append(size)
                size = 0
        return res

        