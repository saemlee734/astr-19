# Write a Python program that prints the sum of two floating point numbers, 
#the difference between two integers, 
#and the product of a floating point number and an integer.
# In each case, have the program print out the data type of the resulting answer.

#Let user know that about first part
print("This code will print the sum of two floating point numbers.")

#Have user input first floating point number
floating_number_input_1 = float(input("Enter your first floating point number: "))

#have user input second floating point number
floating_number_input_2 = float(input("Enter your second floating point number: "))

#take the sum of both floating point numbers
floating_point_sum = floating_number_input_1 + floating_number_input_2

#return sum to user
print("Sum of both floating point numbers: ", floating_point_sum)

#return data type of sum
print("Data type of floating point sum: ", type(floating_point_sum))

#Let user know that this is the second part of the code
print("This code will print the difference between two integers.")

#have user input first integer
integer_1 = int(input("Enter your first integer: "))

#have user input second integer
integer_2 = int(input("Enter your second integer: "))

#calculate difference of integers
integer_difference = integer_1 - integer_2

#return the difference to user 
print("The difference of the two integers is: ", integer_difference)

#return data type of integer difference 
print("The data type of the integer difference is: ", type(integer_difference))

#Let user know that this is part 3 of the code
print("This part of the code will take a floating point number and an integer and calculate the product.")

#get floating point number from user
float_number_part_3 = float(input("Enter a floating point number: "))

#get an integer from the user
integer_part_3 = int(input("Enter an integer: "))

#calculate the product of the two numbers
product_part_3 = float_number_part_3 * integer_part_3

#print the product 
print("Product of floating point number and integer: ",product_part_3)

#return data type 
print("Data type of product: ", type(product_part_3))

#print end
print("This is the end of the code.")

