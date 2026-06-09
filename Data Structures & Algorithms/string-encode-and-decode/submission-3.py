class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            for i in range(len(s)):
                encoded += s[i]
            encoded += "."
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            word = ""
            while s[i] != ".":
                word += s[i]
                i += 1
            i += 1
            res.append(word)
        
        return res

