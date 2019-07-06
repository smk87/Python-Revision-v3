# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function


def sayHello(name, location="Dhaka"):
    print('Hello '+name+' in '+location)


sayHello('Saqlain')

# Return value


def getSum(num1, num2):
    return num1+num2


numSum = getSum(2, 3)

print(numSum)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum=lambda num1, num2: num1+num2
print(getSum(9,2))

addOneToNum=lambda num1:num1+1
print(addOneToNum(16))