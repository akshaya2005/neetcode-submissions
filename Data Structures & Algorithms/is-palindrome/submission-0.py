class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.lower()
        print(s)
        while i <= j:
            if not ((97 <= ord(s[i]) <= 122) or 48 <= ord(s[i]) <= 57):
                i+=1
                continue
            if not ((97 <= ord(s[j]) <= 122) or 48 <= ord(s[j]) <= 57):
                j-=1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
            

        