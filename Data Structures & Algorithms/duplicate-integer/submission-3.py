class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums);
        return len(my_set) != len(nums)

        # my_map = set()

        # for n in nums:
        #     if n not in my_map:
        #         my_map.add(n)
        #     else:
        #         return True
        
        # return False