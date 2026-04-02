class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        prefix = [0] * length
        suffix = [0] * length
        maxTrapped = 0

        for i in range(1, length):
            prefix[i] = max(prefix[i - 1], height[i - 1])
        
        for i in range(length - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i + 1])
        
        for i in range(length):
            trapped = min(prefix[i], suffix[i]) - height[i]
            if trapped > 0:
                maxTrapped += trapped

        return maxTrapped