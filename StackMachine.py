class StackMachine:

    stack = []
    
    def __init__(self):
        self.stack = []

    def push(self,num):
        if len(self.stack) == 0:
            return "None"
        else:
            self.stack.append(num)

    def pop(self):
        return self.stack.pop()

    def add(self):
        if(len(self.stack) == 2):
            ans = int(self.stack[0]) + int(self.stack[1])
            self.stack[0] = ans
            self.stack.pop()

    def sub(self):
        if(len(self.stack) == 2):
            ans = int(self.stack[0]) - int(self.stack[1])
            self.stack[0] = ans
            self.stack.pop()

    def mul(self):
        if(len(self.stack) == 2):
            ans = int(self.stack[0]) * int(self.stack[1])
            self.stack[0] = ans
            self.stack.pop()

    def div(self):
        if(len(self.stack) == 2):
            ans = int(self.stack[0]) / int(self.stack[1])
            self.stack[0] = ans
            self.stack.pop()

    def mod(self):
        if(len(self.stack) == 2):
            ans = int(self.stack[0]) % int(self.stack[1])
            self.stack[0] = ans
            self.stack.pop()


