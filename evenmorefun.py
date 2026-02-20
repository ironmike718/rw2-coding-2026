
# this is a while loop

i = 0
while i < 4:
  i += 1
  if i == 3:
    continue
  print(i)

# this is a tuple, looks like a list, cannot change it though!

cars = ("mercedes", "bmw", "subaru")
print(cars)

print(cars[2])


# dictionaries, key/value pairs

mustang_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

legacy_dict = {"brand": "subaru", "model": "Legacy", "year": 2026}

print(mustang_dict["brand"])

print(legacy_dict["year"])

