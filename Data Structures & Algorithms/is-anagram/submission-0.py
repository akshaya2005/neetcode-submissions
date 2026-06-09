class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        i = defaultdict(int)
        j = defaultdict(int)
        for k in range(len(s)):
            i[s[k]] += 1
            j[t[k]] += 1
        print(i, j)
        for char, count in i.items():
            if j[char] != count:
                return False
        return True
            
        