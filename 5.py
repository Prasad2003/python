#5.	Write a Python script to merge two Python dictionaries.

# Define two sample dictionaries
dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
dict2 = {'country': 'USA', 'job': 'Engineer'}

# Method 1: Using the update() method
merged_dict = dict1.copy()  # Create a copy of dict1
merged_dict.update(dict2)   # Update it with the key-value pairs from dict2

# Method 2: Using dictionary comprehension
merged_dict_comp = {**dict1, **dict2}

# Method 3: Using the merge operator (Python 3.9+)
merged_dict_merge = dict1 | dict2

# Print the merged dictionaries
print("Merged Dictionary (Using update()):", merged_dict)
print("Merged Dictionary (Using dictionary comprehension):", merged_dict_comp)
print("Merged Dictionary (Using merge operator):", merged_dict_merge)
