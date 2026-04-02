class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        l_max = l
        r_max = r

        res = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                if height[l] < height[l_max]:
                    res += height[l_max] - height[l]
                else:
                    l_max = l
            else:
                r -= 1
                if height[r] < height[r_max]:
                    res += height[r_max] - height[r]
                else:
                    r_max = r
        
        return res