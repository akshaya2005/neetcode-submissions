class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        
        arr = sorted(arr)
        stack = []
        stack.append(arr[0])
        for i in range(1, len(arr)):
    
            while stack and (target - stack[-1][0]) / stack[-1][1] <= (target - arr[i][0]) / arr[i][1]:
                stack.pop()
            stack.append(arr[i])
        
        # print(stack)
        return len(stack)




            
        