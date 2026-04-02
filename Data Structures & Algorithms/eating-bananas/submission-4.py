class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)

        while minSpeed < maxSpeed:
            speed = minSpeed + (maxSpeed - minSpeed) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / speed)
            if hours <= h:
                maxSpeed = speed
            else:
                minSpeed = speed + 1
        
        return minSpeed
