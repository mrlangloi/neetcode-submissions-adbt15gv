class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                topTemp = stack.pop()
                res[topTemp[1]] = i - topTemp[1]
            else:
                stack.append((temperatures[i], i))
        
        return res