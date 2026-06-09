class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = []
        res = []

        def helper(nOpen, nClosed):
            print("".join(curr))
            if nOpen == nClosed == n:
                res.append("".join(curr))
                return
            if nOpen < n:
                curr.append("(")
                helper(nOpen + 1, nClosed)
                print("pop", curr[-1])
                curr.pop()
            if nClosed < nOpen:
                curr.append(")")
                helper(nOpen, nClosed + 1)
                print("pop", curr[-1])
                curr.pop()
        
        helper(0, 0)
        return res
        