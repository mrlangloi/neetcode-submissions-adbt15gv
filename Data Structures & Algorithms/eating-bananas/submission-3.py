class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            speed = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / speed)
            if hours <= h:
                r = speed
            else:
                l = speed + 1
        
        return l