import numpy as np

def interpolate(x, data_points):
    # Find the three closest points for quadratic interpolation
    distances = [abs(point[0] - x) for point in data_points]
    closest_indices = sorted(range(len(distances)), key=lambda k: distances[k])[:3]
    closest_points = [data_points[i] for i in closest_indices]

    # Perform quadratic interpolation
    x_values = [point[0] for point in closest_points]
    y_values = [point[1] for point in closest_points]
    coefficients = np.polyfit(x_values, y_values, 2)

    return np.polyval(coefficients, x)

def richardson_extrapolation(reference_point, data_points, tolerance, max_steps, initial_step_size):
    step_sizes = [initial_step_size]
    approximations = [[(interpolate(reference_point + step_sizes[0], data_points) - interpolate(reference_point - step_sizes[0], data_points)) / (2 * step_sizes[0])]]

    for step in range(1, max_steps):
        step_sizes.append(step_sizes[step - 1] / 2)
        approximations.append([(interpolate(reference_point + step_sizes[step], data_points) - interpolate(reference_point - step_sizes[step], data_points)) / (2 * step_sizes[step])])

        for j in range(1, step + 1):
            approximations[step].append((4 ** j * approximations[step][j - 1] - approximations[step - 1][j - 1]) / (4 ** j - 1))

        if step > 0 and abs(approximations[step][step] - approximations[step - 1][step - 1]) <= tolerance:
            return step_sizes[:step+1], approximations[:step+1], True

    return step_sizes, approximations, False  # Return False if tolerance not met

def print_results(tolerance, reference_point, max_steps, initial_step_size, data_points):
    step_sizes, approximations, tolerance_met = richardson_extrapolation(reference_point, data_points, tolerance, max_steps, initial_step_size)

    # Print the results
    print("\nRichardson Extrapolation Results for Derivative:")
    print(f"{'Step':^6}{'Step Size':^15}{'Approximation':^20}")
    print("-" * 41)
    for i, (size, approx) in enumerate(zip(step_sizes, approximations)):
        print(f"{i+1:^6}{size:^15.10f}{approx[-1]:^20.10f}")

    if tolerance_met:
        print(f"\nTolerance of {tolerance} met.")
        print(f"Final approximation of derivative: {approximations[-1][-1]:.10f}")
    else:
        print(f"\nTolerance of {tolerance} not met within {max_steps} steps.")
        print(f"Best approximation of derivative: {approximations[-1][-1]:.10f}")
        if len(approximations) > 1:
            last_difference = abs(approximations[-1][-1] - approximations[-2][-1])
            print(f"Last difference: {last_difference:.10f}")



# Define the inputs for the first example
tolerance1 = 0.0000000001
reference_point1 = 1
max_steps1 = 5
initial_step_size1 = 1
data_points1 = [(0.0, 0.0000000000), (0.5, 0.4794255386), (1.0, 0.8414709848),
                 (1.5, 0.9974949866), (2.0, 0.9092974268)]

# Define the inputs for the second example - When x=0.5 outside the given range of points
tolerance2 = 0.0001
reference_point2 = 0.5
max_steps2 = 10
initial_step_size2 = 0.5
data_points2 = [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Define the inputs for the third example
tolerance3 = 0.0001
reference_point3 = 2
max_steps3 = 10
initial_step_size3 = 0.5
data_points3 = [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Run for the first example
print("Example 1:")
print_results(tolerance1, reference_point1, max_steps1, initial_step_size1, data_points1)

# Run for the second example
print("\nExample 2:")
print_results(tolerance2, reference_point2, max_steps2, initial_step_size2, data_points2)

# Run for the third example
print("\nExample 3:")
print_results(tolerance3, reference_point3, max_steps3, initial_step_size3,data_points3)