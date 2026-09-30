class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = defaultdict(int)
        matched = 0
        k = len(s1)
        l = 0
        for r in range(len(s2)):
            c = s2[r]
            window[c] += 1
            if window[c] <= need[c]:
                matched += 1
            
            # if r + l - 1 >= len(s1):
            #     l += 1
            
            if r >= len(s1):
                
                out = s2[l]
                if window[out] <= need[out]:
                    matched -= 1
                window[out] -= 1

                l += 1
            
           
            if matched == len(s1):
                return True

        return False