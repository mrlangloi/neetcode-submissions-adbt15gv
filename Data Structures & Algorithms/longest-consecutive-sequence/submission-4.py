class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        starts = []
        res = 0
        
        for num in nums_set:
            if num - 1 not in nums_set:
                starts.append(num)
        
        for i in range(len(starts)):
            cont = 0
            while starts[i] + cont in nums_set:
                res = max(res, cont + 1)
                cont += 1
            
        return res