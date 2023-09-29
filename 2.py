def replace_key_value(dictionary, key_to_check, new_key, new_value):
    if key_to_check in dictionary:
        dictionary[new_key] = new_value
        del dictionary[key_to_check]
        return True
    else:
        return False

# Example dictionary
my_dict = {'name': 'John', 'age': 30}

key_to_check = input("Enter the key to check: ")
new_key = input("Enter the new key: ")
new_value = input("Enter the new value: ")

if replace_key_value(my_dict, key_to_check, new_key, new_value):
    print(f"The key '{key_to_check}' was replaced with '({new_key}, {new_value})'.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
    
print("Updated Dictionary:", my_dict)
