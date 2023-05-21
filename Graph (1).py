import matplotlib.pyplot as plt
import numpy as np

# Get input from the user for the function to plot
function_string = input("Enter a function to plot (use 'x' as the variable): ")

# Convert the function string to a callable function
def user_function(x):
    return eval(function_string)

# Define the x range for the graph
x_min = float(input("Enter the minimum x value: "))
x_max = float(input("Enter the maximum x value: "))
x_range = np.arange(x_min, x_max, 0.1)

# Calculate the y values for the graph using the user-defined function
y_values = user_function(x_range)

# Create a figure object and set its size
fig = plt.figure(figsize=(8, 6))

# Create a plot object and plot the data
plt.plot(x_range, y_values)

# Customize the plot by adding labels and a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph Title')

# Show the plot
plt.show()
