class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ## we don't need the whole thing to be sorted
        ## we just need the kth smallest element and then
        ## we have to get the points that are all to the left of it

        class pointDistance:
            def __init__(self, x, y):
                self.point = (x, y)
                self.dist = math.sqrt(x**2 + y**2)
            def __repr__(self):
                return f"x: {self.point[0]}, y: {self.point[1]}, distance: {self.dist}"


        def partition(l, r, points):
           
            ## always choose midpoint to be the pivot
            pivot = (l + r) // 2 
            print(l,r,pivot)
            ## swap l and pivot
            temp = points[pivot]
            points[pivot] = points[l]
            points[l] = temp
        
            i = l + 1
            j = r

            while i <= j:
                while i <= j and points[i].dist <= points[l].dist:
                    i += 1
                while i <= j and points[j].dist >= points[l].dist:
                    j -= 1
                if i <= j:
                    ## swap i and j
                    temp = points[i]
                    points[i] = points[j]
                    points[j] = temp
            temp = points[j]
            points[j] = points[l]
            points[l] = temp
            if j == k - 1:
                return ([[p.point[0], p.point[1]] for p in points[:k]])

            if j < k - 1:
                return partition(j + 1, r, pointDistances)
            else:
                return partition(l, j - 1, pointDistances)

        
        pointDistances = []
        for p in points:
            pointDistances.append(pointDistance(p[0], p[1]))

       
        # print(pointDistances)
        return partition(0, len(points) - 1, pointDistances)
        
            
                




        