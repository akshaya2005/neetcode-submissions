class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for ticket in sorted(tickets)[::-1]:
            adj[ticket[0]].append(ticket[1])
        print(adj)
        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
        
        dfs('JFK')
        return res[::-1]
        