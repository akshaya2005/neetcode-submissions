class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        string = ["("]
        nOpen = 1
        nClosed = 0
        def dfs(string, nOpen, nClosed):
            if nOpen == nClosed == n: # valid string
                res.append("".join(string[:])) 

            if nOpen < n:
                string.append("(")
                dfs(string, nOpen+1, nClosed)
                string.pop()
            if nClosed < nOpen:
                string.append(")")
                dfs(string, nOpen, nClosed+1)
                string.pop()
        dfs(string, nOpen, nClosed)
        return res 

            

        