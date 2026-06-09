class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not (ord('z') >= ord(s[i]) >= ord('a') or ord('Z') >= ord(s[i]) >= ord('A') or ord('0') <= ord(s[i]) <= ord('9')):
                i += 1
            while i < j and not (ord('z') >= ord(s[j]) >= ord('a') or ord('Z') >= ord(s[j]) >= ord('A') or ord('0') <= ord(s[i]) <= ord('9')):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
          
            i += 1
            j -= 1
        return True