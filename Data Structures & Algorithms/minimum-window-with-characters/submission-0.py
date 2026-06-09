class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        we know that the window must start and end with letters from t
        we also know that if we see a duplicate of the first character in the window
        before finding a full substring match we must address it by
        - popping the first element from the seen list
        - updating the left pointer
        - continuing to run the search from j

        1) we create a hashmap that stores the last occurrences of the letters of t
        in s
        2) before the while loop skip past any leading nonviable chars
        3) while i < len(s)
        4) while len(seen) < len(t)
            - grow the window. 
            - if you see a duplicate of s[i]:
            - pop i from seen
            - i = letters[seen[0]]
            
        5) when this inner loop ends (everytime you find a valid substring)
            - check whether it is the max
            - pop first char from seen
            - move i to letters[seen[0]]
    
        """
        if t == "":
            return ""
        countT, window = {}, {}

        ## get counts for the letters in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        ## number of chars from t we have seen, number we still need to see
        have, need = 0, len(countT)

        ## store final res indices and res length
        res, resLen = [-1, -1], float('inf')

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            ## keep growing the window until 
            ## you have all the characters you need
            if c in countT and window[c] == countT[c]:
                have += 1

            ## shrink the window
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""
            
                
            



        