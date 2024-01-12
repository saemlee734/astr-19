'''
Write a Python program that writes out a table of the 
function sin(x) vs. x, where x is tabulated between 0 
and 2 with a thousand entries. Follow the basic Python 
program structure, including a main program function.
'''

# Import the math module to access mathematical functions
import math

# Define a function to generate a table of sin(x) vs. x
def generate_sin_table(start, end, num_entries):

    # Initialize an empty list to store tuples of x and sin(x) values
    table = []
    
    # Loop to generate x and sin(x) values for each entry in the table
    for i in range(num_entries):

        # Calculate x for the current entry using linear interpolation
        x = start + (end - start) * i / (num_entries - 1)
        
        # Calculate sin(x) for the current x value
        sin_value = math.sin(x)
        
        # Append a tuple of (x, sin(x)) to the table list
        table.append((x, sin_value))
    
    # Return the generated table
    return table

# Define a function to print the generated table in a formatted manner
def print_table(table):

    # Print column headers with proper formatting
    print("{:<15} {:<15}".format("x", "sin(x)"))
    
    # Print a line of dashes as a separator
    print("-" * 30)
    
    # Loop to print each entry in the table with proper formatting
    for entry in table:
        print("{:<15.4f} {:<15.4f}".format(entry[0], entry[1]))

# Define the main program function
def main():

    # Set the start, end, and number of entries for the table
    start_x = 0
    end_x = 2

    #stop at 1000 entries 
    num_entries = 1000

    # Generate the sin(x) vs. x table using the specified parameters
    sin_table = generate_sin_table(start_x, end_x, num_entries)

    # Print the generated table
    print_table(sin_table)

# Check if the script is being run as the main program
if __name__ == "__main__":
    
    # Call the main function if the script is executed
    main()
