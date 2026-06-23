class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        countT = defaultdict(int)
        
        for char in t:
            countT[char] += 1
        
        window = defaultdict(int)
        have = 0
        need = len(countT)
        res = [-1, -1]
        resLen = 1000000000
        l = 0
        
        for r in range(len(s)):
            window[s[r]] += 1
            print(window)
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1
            print(have, need)
        
            while have == need:
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
            
                l += 1
            
                if (r - l + 2) < resLen:
                    print("update")
                    resLen = r - l + 2
                    res = [l - 1, r]
            
        return s[res[0] : res[1] + 1]
            




        