# this is a dictionary exercise
teacher = {"name":"mike", "age":"48"}

# add a new dictionary element called city with a value of boston
teacher["city"] = "boston"

# print a sentence to the screen using f-strings that says
# mike is 48 and lives in boston

print(f"{teacher['name']} is {teacher['age']} and lives in {teacher['city']}")

print(teacher["name"] + " is " + teacher["age"] + " and lives in " + teacher["city"])

