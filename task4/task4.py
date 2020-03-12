import sys


# Read file
with open(sys.argv[1]) as f:
    enters = f.readlines()

# Create array res for each minnute in day
res = [0] * 1440

# Convert time into minutes index
for interval in enters:
    start, end = interval.strip().split(' ')

    hours, minutes = start.split(':')
    start_index = int(hours) * 60 + int(minutes)
    
    hours, minutes = end.split(':')
    end_index = int(hours) * 60 + int(minutes)

    for i in range(start_index, end_index + 1):
        res[i] += 1

# Create flags for track continuous time intervals
max_res = max(res)
in_maxres = False
mr_start = None
mr_end = None

for i, e in enumerate(res):
    # Start of the interval
    if e == max_res and in_maxres == False:
        in_maxres = True
        mr_start = i
        mr_end = i
    # Middle of the interval
    elif e == max_res and in_maxres == True:
        mr_end = i
    # End of the interval
    elif e != max_res and in_maxres == True:
        in_maxres = False
        print('{:0>2}'.format(str(mr_start//60)) + ':' + '{:0>2}'.format(str(mr_start%60)) + ' ' + '{:0>2}'.format(str(mr_end//60)) + ':' + '{:0>2}'.format(str(mr_end%60)))
