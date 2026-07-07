class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        curr = []
        res = []
        def helper(numOpen, numClosed):
            if numClosed == numOpen == n:
                res.append("".join(curr[:]))
                return
            if numOpen < n:
                curr.append("(")
                helper(numOpen + 1, numClosed)
                curr.pop()
                
            if numClosed < numOpen:
                curr.append(")")
                helper(numOpen, numClosed + 1)
                curr.pop()
        
        helper(0, 0)
        return res
            
        