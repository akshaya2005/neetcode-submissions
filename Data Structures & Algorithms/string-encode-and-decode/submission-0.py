class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            length = len(word)
            string += str(length) 
            string += "#"
            string += word
        return string



    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i + 1
            while s[j] != "#":   ## j points at the hashtag 4#neet
                j += 1
            length = int(str(s[i:j]))
            j += 1
            result.append(s[j:(j+length)])
            i = j + length
        return result
            