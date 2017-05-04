import sys

print("Assignment #4-1, Alexander Pearson-Goulart, pearsongoulart@gmail.com")

[ print(','.join(x.split())) for x in open(sys.argv[1]).readlines() if len(x.split()) > 0 ]
