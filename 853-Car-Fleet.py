class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[p,s] for p , s in zip(position, speed)]

        for p, s in sorted(pair)[::-1]:
            time = (target - p)/s
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)


    
