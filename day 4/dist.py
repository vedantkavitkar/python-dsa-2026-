# ---------------------- DICTIONARY ----------------------
# di = {1: "VedantKavitkar"}
# print(di) 


di = {101: "Swanand", 102: "Sipna"}

print(di)                 # Print dictionary

print(di.values())        # Print all values

print(di.keys())          # Print all keys

print(di.get(101))        # Get value using key

# di.clear()              # Remove all elements

print(di)

di1 = di.copy()           # Create a copy of dictionary

print(di1)

di1.update({103: "Vedant"})   # Add/Update key-value pair
print(di1)

# ---------------------- DICTIONARY FUNCTIONS ----------------------

di1.pop(101)              # Remove element using key
print(di1)

di1.popitem()             # Remove the last key-value pair
print(di1)

print(di.items())         # Print all key-value pairs

# ---------------------- fromkeys() ----------------------
# Create a dictionary with default value None

keys = ["A", "B", "C"]

di = dict.fromkeys(keys)

print(di)

# ---------------------- update() ----------------------
# Update the value of a key

di.update({'A': "Vedant"})

print(di)

# ---------------------- DICTIONARY ----------------------

# A dictionary stores data in the form of key : value pairs.
# Dictionaries are mutable (elements can be added, updated, or removed).
# Keys must be unique and immutable (int, string, tuple, etc.).
# Values can be of any data type and can be duplicated.
# Dictionaries are created using {} (curly braces).