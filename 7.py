def find_largest_number(a, b, c):
    # Compare a and b, then compare the result with c
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    return largest

# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Call the function to find the largest number
result = find_largest_number(num1, num2, num3)

# Display the result
print("The largest number is:", result)
