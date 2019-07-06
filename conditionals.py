# If/ Else conditions are used to decide to do something based on something being true or false



# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values



# Logical operators (and, or, not) - Used to combine conditional statements




# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object
numbers=[1,2,3,4]
x=3
y=10

# In
if(x in numbers):
    print(x in numbers)

#Not In
if(y not in numbers):
    print(y in numbers)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

#Is
if x is x:
    print(x is y)

#Is not
if x is not y:
    print(x is not y)    