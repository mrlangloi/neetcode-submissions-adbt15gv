class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        res = []

        for i in range(len(cars)):
            res.append((target - cars[i][0]) / cars[i][1])
            if len(res) > 1 and res[-1] <= res[-2]:
                res.pop()
        
        return len(res)