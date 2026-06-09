class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mp = {}
        for i, p in enumerate(position):
            mp[p] = speed[i]
        mp = {item[0]:item[1] for item in sorted(mp.items(), key=lambda item: item[0], reverse=True)}
        stack = []
        print(mp)
        for pos, sp in mp.items():
            time = (target - pos) / sp
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)                

