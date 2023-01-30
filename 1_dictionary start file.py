import random

phonebook = {}  # -> creates a empty dictionary
phonebook = {
    "Chris": "555−1111",  # dictionaries contain {}  whereas lists contain [] brackets #
    "Katie": "555−2222",  # key is on the left, value is on the right # the values can be any object in python #
    "Joanne": "555−3333",
}

"""

mydictionary = dict(m=8, n=9)

print(mydictionary)

print(f"Number of key-value pairs: {len(phonebook)}")




print()
print("*****  start section 1 - print dictionary ********")
print()


print()
print("*****  end section 1 ********")
print()





print()
print("*****  start section 2 - search dictionary ********")
print()

name = "chris"

if name in phonebook:
    print(
        phonebook[name]
    )  # a key error means the key does not exist in the dictionary #

else:
    print(f"{name} does not exist in the phonebook :(")


print()
print("*****  end section 2 ********")
print()




print()
print("*****  start section 3 - edit/append dictionary ********")
print()


print(phonebook)  # keys in a dictionary are unique, there will not be repeat values #

phonebook["Chris"] = "555-444"

phonebook["Joe"] = "555-0123" # new key-value pair was created and appended to the dictionary #

print(phonebook)


print()
print("*****  end section 3 ********")
print()





print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()


print(phonebook)
del phonebook["Chris"]  # if "Chris" does not exist, the del command will error out #
print(phonebook)


print()
print("*****  end section 4 ********")
print()




print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()


for key in phonebook:  # the default in dictionaries for iteration is the key
    print(f"the key is {key} and the value is {phonebook[key]}")

for (
    value
) in (
    phonebook.values()
):  # values is a method of dictionaries that allows iteration through the values of the dictionary
    print(value)

for k, v in phonebook.items():
    print(f"the key is {k} and the value is {k}")

for ph_tuple in phonebook.items(): # without splitting into elements, the output is a tuple
    print(ph_tuple)


print()
print("*****  end section 5 ********")
print()





print()
print("*****  start section 6 - using get and clear ********")
print()

name = "chris"

phone = phonebook.get(name, "key not found") # if found, print key; if not found, print message

print(phone)

phonebook.clear()
print(phonebook)


print()
print("*****  end section 6 ********")
print()



print()
print("*****  start section 7 - using pop method ********")
print()


remove = phonebook.pop("Chris", "not found")

print(remove)
print(phonebook)


print()
print("*****  end section 7 ********")
print()



print()
print("*****  start section 8 - using popitem ********")
print()


a = phonebook.popitem() # supposed to be random, but pops the last item
print(a)
print(phonebook)


print()
print("*****  end section 8 ********")
print()



print()
print("*****  start section 9 - using random and converting to list ********")
print()


list_of_keys = list(
    phonebook
)  # creates a list of keys because that is default value for dictionaries
random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook[random_key])


print()
print("*****  end section 9 ********")
print()

"""
print((phonebook[random.choice(list(phonebook))]))  # doing section 9 in one line
