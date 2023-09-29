#9.	Write a Python function that accepts a string and counts the number of upper and lower case letters.

def count_upper_lower_case(input_string):
    # Initialize variables to count uppercase and lowercase letters
    upper_count = 0
    lower_count = 0

    # Iterate through each character in the string
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Example string
my_string = "Hello World"

# Call the function to count uppercase and lowercase letters
upper, lower = count_upper_lower_case(my_string)

# Display the results
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
