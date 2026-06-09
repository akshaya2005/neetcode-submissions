class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        ## you want the substring to always have the same characters
        """
        look at xy x and y are different so pick a letter to transform
        lets pick x and change the y into an x
        for this value of l this is waht we will compare the s[r] to

        while n > 0
        you may change any future nonmatching characters into X and increase
        the length of the string but after you have made as many changes as possible 
        do you skip past all the characters you just saw or look for overlapping problems
        move l to one past the first character that was altered
        always default to setting r character to l character when there is a mismatch


        if you have AXXB the optimal solution is to change a and b so that
        you can have AAAA how do you handle this case?

        """
        count = defaultdict(int)
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count[s[r]]
            maxf = max(maxf, count[s[r]])
            
            ## if there aren't enough replacements to rectify this string
            ## move l over by 1 and decrement the count of s[l]
            while (r-l+1)- maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
                    
        
                    
            


            
                


        