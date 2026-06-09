class Solution:
    class pointDistance:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.dist = math.sqrt(x*x + y*y)
        def __lt__(self, other):
            ## want closest points
            return self.dist < other.dist

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointDistances = []
        res = []
        for x,y in points:
            pd = self.pointDistance(x,y)
            pointDistances.append(pd)

        heapq.heapify(pointDistances)
        for i in range(k):
            pd = heapq.heappop(pointDistances)
            res.append([pd.x, pd.y])
        return res


        

        

        