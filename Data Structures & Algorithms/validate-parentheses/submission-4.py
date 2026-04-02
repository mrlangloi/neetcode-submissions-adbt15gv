class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in brackets:
                if len(stack) > 0:
                    if stack[-1] == brackets[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0