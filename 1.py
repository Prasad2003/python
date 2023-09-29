def generate_squared_dict(n):
    squared_dict = {}
    for x in range(1, n + 1):
        squared_dict[x] = x * x
    return squared_dict

n = int(input("Enter a number (n): "))
result_dict = generate_squared_dict(n)

for key, value in result_dict.items():
    print(f"({key}, {value})")
