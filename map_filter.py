values = [1, 2, 3, 4, 5]

doubled_values = list(map(lambda x: x * 2, values))
odd_values = list(filter(lambda x: x % 2, values))

print(doubled_values) # Prints: [2, 4, 6, 8, 10]
print(odd_values) 