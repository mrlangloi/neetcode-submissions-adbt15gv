class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        left = 0

        for i in range(len(prices)):
            if prices[i] < prices[left]:
                left = i
            res = max(res, prices[i] - prices[left])

        return res