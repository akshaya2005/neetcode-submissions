class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## every car can catch up to a car in front of it
        fleets = 0
        stack = []
        class item:
            def __init__(self, position, speed, time):
                self.position = position
                self.speed = speed
                self.time = time
            
            def __lt__(self, other):
                return self.position < other.position
            
            def __repr__(self):
                return f"Position: {self.position}/Speed: {self.speed}/Time: {self.time}\n"
        arr = []
        for i in range(len(position)):
            arr.append(item(position[i], speed[i], (target - position[i]) / speed[i]))
        
        arr = sorted(arr)
        print(arr)
        stack.append(arr[0])
        for obj in arr[1:]:
            while stack and stack[-1].time <= obj.time:
                stack.pop()
            stack.append(obj)
        
        return len(stack)
        
            

            