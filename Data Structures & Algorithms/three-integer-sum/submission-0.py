class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums_sorted = sorted(nums)

        for i in range(len(nums_sorted)):
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = -(nums_sorted[i])
            while l < r:
                two_sum = nums_sorted[l] + nums_sorted[r]
                if two_sum == target:
                    res.append([-target, nums_sorted[l], nums_sorted[r]])
                    while l < r and nums_sorted[l] == nums_sorted[l + 1]:
                        l += 1
                    while l < r and nums_sorted[r] == nums_sorted[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                    continue
                elif two_sum > target:
                    r -= 1
                else:
                    l += 1
        
        return res