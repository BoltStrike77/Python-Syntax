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

# Numbers
x = 1    # int, whole positive or negative number
y = 2.8  # float, positive of negative number with one or more decimal digits
z = 1j   # complex, with the j as the imaginary number "i"

# you can convert using
a = 2
a = float(a)
print(a)

# you can use random too
import random
print(random.randrange(1,10));

# Booleans (same as Java but capitalized)
# these all return true
bool("abc")
bool(123)

# only empty values, 0, and None return false
bool(0)

# Operators that are not found in Java
x = 2
y = 2
a = x ** y # exponents, a = 4
a = x // y # divides and rounds to nearest whole, a = 1;

# Assignment operators are just normal operatos but equals after, they assign and do the task
x = 5
x -= 5
x % 5
x /= 5

# Python Identity Operators (same memory location not object)
bool(x is y)
bool(x is not y)


