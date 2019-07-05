# A List is a collection which is ordered and changeable. Allows duplicate members.
# Create List
number = [1, 2, 3, 4, 5]

# Using constructor
numbers = list((1, 2, 3, 4, 5))  # Alternative way, not popular
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

print(fruits[1])

# Get len
print(len(fruits))


# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Pears')

# Insert into list
fruits.insert(2, "Strawberries")

print(fruits)


# Remove from position
fruits.pop(3)

# Reverse list
fruits.reverse()

print(fruits)


# Sort list
fruits.sort()

# Reveres sort()
fruits.sort(reverse=True)

print(fruits)
