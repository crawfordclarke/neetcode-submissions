class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opperand = "+-*/"

        for t in tokens:
            if t not in opperand:
                stack.append(int(t))
            if t in opperand:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    res = a + b
                elif t == "-":
                    res = a - b
                elif t == "*":
                    res = a * b
                else: 
                    res = int(a / b) 
                stack.append(res)
        return stack[-1]
        

        