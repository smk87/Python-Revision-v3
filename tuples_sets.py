# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# $imple Tupple
fruit_tuple = ('Apple', 'Orange', 'Mango')

# Cons Tupple
fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

# Get single value
print(fruit_tuple[1])

# Can not change value

# Tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',)
print(fruit_tuple_2)
# del fruit_tuple  # Delete tuple

# Get leng
print(len(fruit_tuple))

print(fruit_tuple)


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruit_set = {'Apple', 'Orange', 'Mango'}

print(fruit_set)

# Check if in set
print('Apples' in fruit_set)

# Add to set
fruit_set.add('Grape')
print(fruit_set)

# Remove from set
fruit_set.remove('Grape')
print(fruit_set)

# Clear set
fruit_set.clear()

# Delete set
# del fruit_set

print(fruit_set)
