class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            twoSum = numbers[start] + numbers[end]
            if twoSum > target:
                end -= 1
            elif twoSum < target:
                start += 1
            else:
                return [start + 1, end + 1]