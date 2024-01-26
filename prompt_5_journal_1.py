'''
Write a Python program that writes out a table of the 
function sin(x) vs. x, where x is tabulated between 0 
and 2 with a thousand entries. Follow the basic Python 
program structure, including a main program function.
'''

# Import necessary libraries
import numpy as np
from tabulate import tabulate

def generate_sine_table(start, end, num_points):

#Generate a table of sin(x) vs x
#start: Start value for x
#end: End value for x
#num_points: Number of points for tabulation

    x_values = np.linspace(start, end, num_points)
    # Generate x values

    sine_values = np.sin(x_values)
    # Calculate sin(x) values

    # Create a list of tuples with (x, sin(x)) pairs
    table_data = list(zip(x_values, sine_values))
    return table_data

def main():
    # Set the range and number of points
    start_x = 0
    end_x = 2
    num_points = 1000

    # Generate the sine table
    sine_table = generate_sine_table(start_x, end_x, num_points)

    # Define table headers
    headers = ["x", "sin(x)"]

    # Use tabulate to create a formatted table
    table = tabulate(sine_table, headers, tablefmt="fancy_grid")

    # Print the table
    print(table)

if __name__ == "__main__":
    main()
