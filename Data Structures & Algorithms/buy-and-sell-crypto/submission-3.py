class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        highest = prices[0]
        res = 0

        for price in prices:
            if price < lowest:
                lowest = price
            else:
                currentPrice = price - lowest
                res = max(res, currentPrice)
        
        return res