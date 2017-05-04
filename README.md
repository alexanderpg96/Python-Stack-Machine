Assignment 4
============

This assignment builds a stack machine and reads from an external file that instructs the program what to do (ie push, pop, add, etc).

Prog4_1.py
----------

Prog4_1.py opens and reads a file, and then tokenizes each line of the file. It then prints each line that was tokenized to stdout.

StackMachine.py
---------------

StackMachine.py creates a stack machine. It instantiates an empty list, which can then be pushed into, popped, added to, subtracted from, multplied to, divided from, and modded from.

Prog4_2.py
----------

Prog4_2.py opens and reads a file, tokizes each line of the file, and then loops through those lines. If the there is a line of 2 tokenized items, and the first token is "push", the number following is pushed. If it is of length 1, the stack is either popped, added, subbed, multiplied, divided, or modded. If the stack is attempted to pop with nothing on it, "None" is returned as the value.