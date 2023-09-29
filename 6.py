# Define a sample dictionary with numeric values
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# Initialize a variable to store the sum
total_sum = 0

# Iterate through the values of the dictionary and add them to the total_sum
for value in my_dict.values():
    total_sum += value

# Print the sum
print("Sum of all items in the dictionary:", total_sum)
