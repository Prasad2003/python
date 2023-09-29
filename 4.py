# Define three sample dictionaries
dict1 = {'name': 'John', 'age': 30}
dict2 = {'city': 'New York', 'country': 'USA'}
dict3 = {'job': 'Engineer', 'salary': 60000}

# Method 1: Using the update() method
merged_dict = {}
merged_dict.update(dict1)
merged_dict.update(dict2)
merged_dict.update(dict3)

# Method 2: Using dictionary comprehension
merged_dict_comp = {key: value for d in (dict1, dict2, dict3) for key, value in d.items()}

# Method 3: Using the ** unpacking operator (Python 3.5+)
merged_dict_unpack = {**dict1, **dict2, **dict3}

# Print the merged dictionaries
print("Merged Dictionary (Using update()):", merged_dict)
print("Merged Dictionary (Using dictionary comprehension):", merged_dict_comp)
print("Merged Dictionary (Using ** unpacking operator):", merged_dict_unpack)
