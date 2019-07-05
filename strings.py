# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Saqlain"
age = 23

# Concat
print("Hello I am "+name+" and I am "+str(age))

# Arguments by position
print('{},{},{}'.format("a", "b", "c"))
print('{2},{0},{1}'.format("a", "b", "c"))

# Arguments by name
print('My name is {name} and I am {age}'.format(name="Saqlain", age=age))

# F-String(v3.6+)
print(f"My name is {name} and I am {age}")

# String Methods
s = "hello world"

# Capatilize first letter
print(s.capitalize())

# Make all uppper
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get lenght
print(len(s))

# Replace
print(s.replace("world", "all"))


# String Formatting

# String Methods
