class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        prefix = [101] * len(prices)
        res = 0

        prefix[0] = prices[0]

        for i in range(1, len(prices)):
            prefix[i] = min(prefix[i - 1], prices[i])
        
        for i in range(len(prices)):
            res = max(res, prices[i] - prefix[i])
        
        return res