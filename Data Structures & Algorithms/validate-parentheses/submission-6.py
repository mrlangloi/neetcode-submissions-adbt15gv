class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"]": "[", "}": "{", ")": "("}
        stack = []

        for b in s:
            if b not in brackets:
                stack.append(b)
            else:
                if stack and stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0