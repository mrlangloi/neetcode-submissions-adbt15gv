class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_dict:
                return [nums_dict.get(diff), i]
            else:
                nums_dict[nums[i]] = i
        
        return []