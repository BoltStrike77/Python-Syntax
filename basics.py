# All if not most examples are from w3schools

# Integer print
num = 2;
print(num)

# String print
string = "hello world"
print(string)

# Conditional
if 5 > 2:
    print("Five is greater than two!")

# Casting
x = 5
x = str(x)
print(x)

# Single or double quotes are the same in Python
# Dashes, spaces, and numbers are illegal variable names

x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"

# Unpacking list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# To print multiple values, try commas
x = 5
y = "John"
print(x, y)

# Functions
temp = "dang"
def variableTest():
    temp = "dank"
    print("Local overrides global: " + temp)
    # this local variable overrides the global variable

variableTest()

# Types
x = "Hello World" #str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True #bool	
x = b"Hello" #bytes	
x = bytearray(5) #bytearray	
x = memoryview(bytes(5)) #memoryview	
x = None #NoneType	

# You can also set specific data types
x = str("Hello World")
x = int(2)
