# Numbers, Strings, Booleans

# Numbers = integers. floats, longs(depreciated), double, complex
# Strings = Any text "" or ''
# Boolean = True or False

# Operators
# Arithmetic and Comparative

# Arithmetic Operators:
# + adds two variables together
# - subtracts two variables together
# * multiplies 2 variables together
# / divided two variables together
# % remainder of a division of the left variable by the right variable.

# Comparison Operators:
# > True if the left is greater than the right
# < Other waya round
# ==  equal to
# !=  Not equal to
# >= True if left operand greater or equal to the right
# <= True if left variable is less than or equal to the right

# Numeric Types

# a = 24
# b = 16
# print(a + b)
# print(a - b)
# print(a > b)
# print(a < b)
#
# # Floats
#
# floatnum = 3.5
# intnum = 3
#
# print(floatnum + intnum)
#
# one_third = 1 / 3
# print(one_third)
#
# print(one_third * 3)
#
# isthisafloat = one_third * 3
# print(type(isthisafloat))
#
# print("Input two number to add: ")
# x = int(input())
# y = int(input())
# print(x + y)
#
# print("Input two number to subtract: ")
# x = int(input())
# y = int(input())
# print(x - y)
#
# print("Input two number to divide: ")
# x = int(input())
# y = int(input())
# print(x / y)
#
# print("Input two number to multiply: ")
# x = int(input())
# y = int(input())
# print(x * y)

Single_Quotes = 'Look! Single Quotes'
Double_Quotes = "Look! Double's Quotes"

print(Single_Quotes)
print(Double_Quotes)

String_Failure = "I said 'Wow'"
print(String_Failure)

escape_example = 'I said \'Wow!\''

# String Slicing

Hw = "Hello! World"
# H e l l o ! W o r l d
# 0 1 2 3 4 5 6 7 8 9 10 11
#

# print(Hw[:10])

# print(len(Hw))

# String Methods

example_text = "Here's some text with lots of text"

print(example_text.upper())
print(example_text.lower())
print(example_text.count("e"))
print(example_text.replace("with", ","))

# Concantenation

x = 2
y = 5.4
z = "there's now a number 25.4 unless we put a space in!"

print(str(x) + " " + str(y) + z)

# f-strings

# Python 3.6 onwards, string that you can bring variable into without casting

name = "Lassie"
years = 7
height_cm = 60.2
print(f"{name} is {years} years old and {height_cm} cm tall")

# We can use methods in a string using f-string

name2 = "Snoopy"
age2 = 52

print(f"{name2.upper()} is {age2 * 7} YEARS OLD IN DOG YEARS")

pi = 3.14159265359
max_score = 26
print(f"Pi to 3 decimal places: {pi:3f}")
print(f"Pi to 7 decimal places: {pi:7f}")
score = 16
print(f"You scored {score / max_score}")
print(f"You scored {score / max_score:%}")
print(f"You scored {score / max_score:.2%}")

# Booleans

a = True
b = False

print(a == b)  # False
print(a != b)  # True

print(True and False)  # False - Both conditions needs to be True!
print(True and True)  # True
print(False or True)

# Booleans with strings

hi = "HelloWorld"

print(hi.isalpha())
print(hi.endswith("!"))

# None in Python
print(type(None))
# print(type(Null))
def check_return():
	pass
print(check_return())

# When there no return statements, None is outputted
# None is similar to a null value if you know anything about those. Someone might say# it's equal to 0, but None means that it is nothing. Say age = None for example. age is a variable, but it is equal to nothing. False is an actual value.
