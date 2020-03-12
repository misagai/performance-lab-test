import os
import sys


# Read files from directory
names = [
    sys.argv[1] + os.sep + 'Cash1.txt',
    sys.argv[1] + os.sep + 'Cash2.txt',
    sys.argv[1] + os.sep + 'Cash3.txt',
    sys.argv[1] + os.sep + 'Cash4.txt',
    sys.argv[1] + os.sep + 'Cash5.txt',
]

# Open each file, convert them into array and sum by index
result = [0] * 16
for name in names:
    with open(name) as f:
        cash = f.readlines()
    cash = [float(n) for n in cash]
    for i, c in enumerate(cash):
        result[i] += c

# Result + 1 - because first index = 0         
print(result.index(max(result)) + 1)