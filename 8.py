def sum_list_numbers(input_list):
    total = 0  # Initialize a variable to store the sum
    
    # Iterate through the list
    for number in input_list:
        if isinstance(number, (int, float)):  # Check if the element is a number
            total += number  # Add the number to the total
    
    return total

# Example list of numbers
my_list = [1, 2, 3, 4, 5.5, 6.5]

# Call the function to sum the numbers in the list
result = sum_list_numbers(my_list)

# Display the result
print("Sum of numbers in the list:", result)
