class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for string in strs:
            s = "".join(sorted(string))
            if s in mp:
                mp[s].append(string)
            else:
                mp[s] = [string]
        
        return list(mp.values())
        


        