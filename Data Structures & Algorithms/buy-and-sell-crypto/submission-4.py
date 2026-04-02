class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0

        for p in prices:
            if p < lowest:
                lowest = p
            else:
                res = max(res, p - lowest)
        
        return res