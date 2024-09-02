

# Define the function for interpolation
def interpolate(x, points):
    # Perform linear interpolation between points
    points.sort()  # Ensure points are sorted by x
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    raise ValueError("x is out of bounds")

# Input values
eps = float(input('Enter the allowed tolerance: '))
x0 = float(input('Enter the value of reference point: '))
n = int(input('Enter the number of steps: '))
points = []

# Read points from user input
print('Enter the points (x, f(x)) separated by a space. Type "done" when finished:')
while True:
    line = input()
    if line.lower() == "done":
        break
    x, y = map(float, line.split())
    points.append((x, y))

# Initial approximation
h1 = [float(input('Enter the initial approximation: '))]
g = [[(interpolate(x0 + h1[0], points) - interpolate(x0 - h1[0], points)) / (2 * h1[0])]]

#Richardson extrapolation process
for i in range(1, n):
    h1.append(h1[i - 1] / 2)
    g.append([(interpolate(x0 + h1[i], points) - interpolate(x0 - h1[i], points)) / (2 * h1[i])])

    for j in range(1, i + 1):
        g[i].append((4 ** j * g[i][j - 1] - g[i - 1][j - 1]) / (4 ** j - 1))

    if abs(g[i][i] - g[i][i - 1]) <= eps:
        break
    elif i == n - 1:
        raise Exception('Richardson extrapolation failed to converge')

# Print the results
print("h1 values:")
for value in h1:
    print(value)

print("\ng values:")
for row in g:
    print(row)

# Print the table
print("\nTable (h1, g):")
for i in range(len(h1)):
    row = [h1[i]] + g[i]
    print(row)
