class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numsSet = set(nums)
        res = 0

        for c in nums:
            length = 0
            if c - 1 in numsSet:
                continue
            elif c + 1 in numsSet:
                
                while c + 1 + length in numsSet:
                    length += 1

            res = max(res, length + 1)

        
        return res