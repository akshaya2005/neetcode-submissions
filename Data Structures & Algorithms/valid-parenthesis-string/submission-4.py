class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = [[None] * (n + 1) for _ in range(n + 1)]
        ## i, open tells you whether a valid string is possible with
        ## the first i characters of the string and having open
        ## open parentheses
        def dfs(i, open):
            if open < 0:
                return False
            if i == n:
                return open == 0
            if memo[i][open] is not None:
                return memo[i][open]

            if s[i] == "(":
                result = dfs(i + 1, open + 1)
            elif s[i] == ")":
                result = dfs(i + 1, open - 1)
            else:
                result = (dfs(i + 1, open) or
                          dfs(i + 1, open + 1) or
                          dfs(i + 1, open - 1))

            memo[i][open] = result
            return result

        return dfs(0, 0)