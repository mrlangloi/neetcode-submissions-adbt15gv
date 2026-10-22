class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for i in range(len(position)):
            #print(f"pos: {cars[i][0]}, speed: {cars[i][1]}")
            time = (target - cars[i][0]) / cars[i][1]
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
            
        return len(stack)