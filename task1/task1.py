import math
import sys


# Read file
with open(sys.argv[1]) as f:
    numbers = f.readlines()

numbers = [int(n) for n in numbers]

# Using the library math we find 90-percentile
size = len(numbers)
percentile = sorted(numbers)[int(math.ceil((size * 90) / 100)) - 1]
print(format(percentile, '.2f'))

# Find median - the middle of the sorted array
num_numbers = len(numbers)
sorted_numbers = sorted(numbers)
if num_numbers % 2 == 0:
    middle = int((num_numbers / 2))
else:
    middle = int((num_numbers / 2) + 0.5)
print(format(sorted_numbers[middle], '.2f'))

# Max number
print(format(max(numbers), '.2f'))

# Min number
print(format(min(numbers), '.2f'))

# Average number
print(format((sum(numbers)/len(numbers)), '.2f'))