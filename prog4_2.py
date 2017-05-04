import sys
from StackMachine import StackMachine

print("Assignment #4-2, Alexander Pearson-Goulart, pearsongoulart@gmail.com")

stack = StackMachine()

f = open(sys.argv[1])
lines = f.readlines()
f.close()

lines[0].split() ## tokenizes a string

tokenized_lines = []

for l in lines:
    tokenized_lines.append(l.split())

for line in tokenized_lines:
    if len(line) == 1:
        if line[0] == "add":
            stack.add()
        elif line[0] == "sub":
            stack.sub()
        elif line[0] == "mul":
            stack.mul()
        elif line[0] == "div":
            stack.div()
        elif line[0] == "mod":
            stack.mod()
        elif line[0] == "pop":
            print(stack.pop())
    elif len(line) == 2:
        if line[0] == "push":
            stack.push(line[1])


