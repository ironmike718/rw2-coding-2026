"""
name = "Gwen"
print("My friend is: " + name)

# welcome to fstrings
print(f"My friend is: {name}")


user_name = input("What is your name? ")
num_1 = input("Give me a number ")
num_2 = input("Give me another number ")

total = float(num_1) + float(num_2)
#str(total)

print(f"Your name is: {user_name} and the total is {total}")

"""

# let's create functions and learn about global/local variables

"""
name = "Josh"
age = 25
city = "KC"

# this is how to create your own function, a block of code
def my_func_1(city):
    name = "Brea"
    age = 21
    city = "Independence"
    print(name, age, city)

print(name, age, city)

my_func_1(city)

"""

my_cars = ["mercedes", "bmw", "subaru", "ford", "chrysler", "porsche"]
print(my_cars)

print(f"i drive a {my_cars[2]}")

print(len(my_cars))

my_cars.append("corvette")
print(len(my_cars))
print(my_cars)


# python "for" loop, control by length of entire list

counter = 0
for car in my_cars:
    print(f"car # {counter} is {car}")
    counter += 1

print("***************")

# python for loop, controlled by range of #'s

my_range = range(4)
for val in my_range:
    print(f"car # {val} is {my_cars[val]}")



