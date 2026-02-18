
# the hash is a one line comment, nothing here executes

"""
the triple quotes are a multi-line comment
see
believe me
anything inside will not execute
"""

# this will print to the screen
# print("Hello Hello Class!")

# variables store information

name = "Gwen"
name_2 = "Lupe"
name_3 = "Brea"

print(name)
print(name_2)
print(name_3)

# this is how we concatenate strings, use a ,
print("In class tonight we have", name, name_2, name_3)

# this is how we concatenate strings, use the +
print("In class tonight we have " + name + " " + name_2 + " and " + name_3)


# common data types

# float
price = 5.99

# integer
age = 35

# boolean
is_here = True

# string
name = "Mike"

# print all the data types

print(type(price))
print(type(age))
print(type(is_here))
print(type(name))

print("Mike's age is " + str(age))


# this is the basic python if statement
if age > 36:
    print("you are an unc")


# this is a more complex python if statement
"""
if age > 36:
    print("you are an unc")
else:
    print("you are not an unc")
"""

age = 99

# this is an even more complex python if statement
if age > 36:
    print("you are an unc")
elif age < 34:
    print("you are not an unc")
else:
    print("you must be 35 years old")

# python operators arithmetic and comparision
"""
arithmetic:  + add, - subtract, * multiplication, / division

comparison:  == equal, != not equal, > greater than, < less than, >= GT or Eq, <= LT or Eq
"""

print(5 + 5)
print(10 - 8)
print(81 / 9)

num_1 = 9
num_2 = 8 
total = num_1 + num_2

print("The total of num_1 and num_2 is: " + str(total))