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

name = "Josh"
age = 25
city = "KC"

def my_func_1(city):
    name = "Brea"
    age = 21
    city = "Independence"
    print(name, age, city)

print(name, age, city)

my_func_1(city)




