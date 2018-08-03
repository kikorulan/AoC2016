# Read data
file_obj = open("input_data_03.dat", "r")
data = file_obj.readlines()

#==================================================
# COUNT TRIANGLES
#==================================================
sides = [0, 0, 0]
count_triangles = 0
for line in data:
    triangle = line.split()
    # Convert to integer
    for i in range(3):
        sides[i] = int(triangle[i])
    # Sort
    sides.sort()
    # Check if it defines a triangle
    if sides[0] + sides[1] > sides[2]:
        count_triangles += 1

print('There are ', count_triangles, ' triangles. - PART 1')

#==================================================
# PART B
#==================================================
count_triangles = 0
counter = 0
for line in data:
    counter += 1
    if counter % 3 == 1:
        line1 = line.split()
    elif counter % 3 == 2:
        line2 = line.split()
    elif counter % 3 == 0:
        line3 = line.split()
        # Build triangles
        triangle1 = [int(line1[0]), int(line2[0]), int(line3[0])]
        triangle2 = [int(line1[1]), int(line2[1]), int(line3[1])]
        triangle3 = [int(line1[2]), int(line2[2]), int(line3[2])]
        # Sort triangles
        triangle1.sort()
        triangle2.sort()
        triangle3.sort()
        print(counter, triangle1)
        print(counter, triangle2)
        print(counter, triangle3)
        if triangle1[0] + triangle1[1] > triangle1[2]:
            count_triangles += 1
        if triangle2[0] + triangle2[1] > triangle2[2]:
            count_triangles += 1
        if triangle3[0] + triangle3[1] > triangle3[2]:
            count_triangles += 1

print('There are ', count_triangles, ' triangles. - PART 2')
