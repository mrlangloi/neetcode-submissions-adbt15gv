class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for t in tokens:
            if t in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                res = 0
                if t == "+":
                    res = op1 + op2
                elif t == "-":
                    res = op1 - op2
                elif t == "*":
                    res = op1 * op2
                else:
                    # using // performs rounding, which we don't want
                    res = int(op1 / op2)
                stack.append(res)
            else:
                stack.append(int(t))
        
        return stack.pop()