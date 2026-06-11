class MinStack:

    def __init__(self):
        self.Stack = []
        self.Min_Stack = []

    def push(self, val: int) -> None:
        self.Stack.append(val)
        if not self.Min_Stack:
            self.Min_Stack.append(val)
        else:
            self.Min_Stack.append(min(val, self.Min_Stack[-1]))

    def pop(self) -> None:
        self.Stack.pop() 
        self.Min_Stack.pop()
        

    def top(self) -> int:
        return self.Stack[-1]
        

    def getMin(self) -> int:
        return self.Min_Stack[-1]
        
