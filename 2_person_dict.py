person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

print(person["children"][1])  # name of second child
print(person["pets"]["cat"])  # name of cat

# list all of the children using a for loop
for i in person["children"]:
    print(i)

# print all of the pets
for key, value in person["pets"].items():
    print(f"Type of pet: {key}, Name of pet: {value}")
