class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def helper(nOpen, nClosed):
            if nOpen == nClosed == n:
                res.append("".join(curr[:]))
            if nOpen < n:
                curr.append("(")
                helper(nOpen + 1, nClosed)
                curr.pop()
                
            if nClosed < nOpen:
                curr.append(")")
                helper(nOpen, nClosed + 1)
                curr.pop()
        
        helper(0,0)
        return res
        