class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0

        for p in range(len(prices)):
            if prices[p] < prices[l]:
                l = p
            res = max(res, prices[p] - prices[l])
        
        return res