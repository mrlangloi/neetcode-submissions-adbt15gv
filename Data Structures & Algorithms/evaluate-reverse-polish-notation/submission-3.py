class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        operators = {"+", "-", "*", "/"}

        for t in tokens:
            if t in operators:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                match t:
                    case "+":
                        res = op1 + op2
                    case "-":
                        res = op1 - op2
                    case "*":
                        res = op1 * op2
                    case "/":
                        res = op1 / op2
                stack.append(res)
            else:
                stack.append(t)
        
        return int(stack[0])