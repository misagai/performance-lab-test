import sys


# Read file 1
with open(sys.argv[1]) as f:
    fpoints = f.readlines()

fpoints = [coord.split(' ') for coord in fpoints]

fpoint1 = (float(fpoints[0][0]), float(fpoints[0][1]))
fpoint2 = (float(fpoints[1][0]), float(fpoints[1][1]))
fpoint3 = (float(fpoints[2][0]), float(fpoints[2][1]))
fpoint4 = (float(fpoints[3][0]), float(fpoints[3][1]))

# Read file 2
with open(sys.argv[2]) as f:
    points = f.readlines()

points = [coord.split(' ') for coord in points]
points = [(float(x), float(y)) for x, y in points]

for point in points:

    # Split the quadrangle to two triangles for simple inside-checks
    pl1 = (fpoint1[0] - point[0]) * (fpoint2[1] - fpoint1[1]) - (fpoint2[0] - fpoint1[0]) * (fpoint1[1] - point[1])
    pl2 = (fpoint2[0] - point[0]) * (fpoint4[1] - fpoint2[1]) - (fpoint4[0] - fpoint2[0]) * (fpoint2[1] - point[1])
    pl3 = (fpoint4[0] - point[0]) * (fpoint1[1] - fpoint4[1]) - (fpoint1[0] - fpoint4[0]) * (fpoint4[1] - point[1])

    pl4 = (fpoint3[0] - point[0]) * (fpoint2[1] - fpoint3[1]) - (fpoint2[0] - fpoint3[0]) * (fpoint3[1] - point[1])
    pl5 = (fpoint2[0] - point[0]) * (fpoint4[1] - fpoint2[1]) - (fpoint4[0] - fpoint2[0]) * (fpoint2[1] - point[1])
    pl6 = (fpoint4[0] - point[0]) * (fpoint3[1] - fpoint4[1]) - (fpoint3[0] - fpoint4[0]) * (fpoint4[1] - point[1])

    # Point is on the vertex
    if point == fpoint1 or point == fpoint2 or point == fpoint3 or point == fpoint4:
        print('0')
        
    # Point is on the edge
    elif ((point[0] - fpoint1[0]) * (fpoint2[1] - fpoint1[1])) == ((point[1] -  fpoint1[1]) * (fpoint2[0] - fpoint1[0])):
        print('1')
    elif ((point[0] - fpoint3[0]) * (fpoint2[1] - fpoint3[1])) == ((point[1] -  fpoint3[1]) * (fpoint2[0] - fpoint3[0])):
        print('1')
    elif ((point[0] - fpoint3[0]) * (fpoint4[1] - fpoint3[1])) == ((point[1] -  fpoint3[1]) * (fpoint4[0] - fpoint3[0])):
        print('1')
    elif ((point[0] - fpoint1[0]) * (fpoint4[1] - fpoint1[1])) == ((point[1] -  fpoint1[1]) * (fpoint4[0] - fpoint1[0])):
        print('1')

    # Point is inside
    elif pl1 > 0 and pl2 >= 0 and pl3 > 0:
        print('2')
    elif pl1 < 0 and pl2 <= 0 and pl3 < 0:
        print('2')
    elif pl4 > 0 and pl5 >= 0 and pl6 > 0:
        print('2')
    elif pl4 < 0 and pl5 <= 0 and pl6 < 0:
        print('2')

    # Point is outside
    else:
        print('3')