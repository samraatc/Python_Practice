
#Dictionaries in Python are versatile and powerful data structures that store key-value pairs. They are mutable, unordered collections that allow for fast lookups, insertions, and deletions based on keys. 
# Here’s a comprehensive overview of dictionaries, including their properties, common operations, methods, and use cases.
#
# 
#   Creating Dictionaries
#A dictionary is created by enclosing key-value pairs in curly braces {}, with a colon : separating each key from its value.
#



# Empty dictionary
empty_dict = {}

# Dictionary with string keys and integer values
student_ages = {
    "Samraat": 21,
    "Ram": 22,
    "Anish": 23
}

# Dictionary with mixed data types
mixed_dict = {
    "name": "Samraat",
    "age": 21,
    "is_student": True
}

# Dictionary with tuple keys
tuple_key_dict = {
    (1, 2): "Coordinates",
    (3, 4): "Another Coordinate"
}
# print (tuple_key_dict)

# can access values in a dictionary using their corresponding keys. 
# If the key does not exist, it raises a KeyError.
student_age = {
    "Samraat": 21,
    "ram": 22,
}

# Samraat_age = student_ages["Samraat"]  # 21
# ram_age = student_ages["ram"]  # 22
# non_existent_age = student_ages["Charlie"]  # This raises a KeyError

#Adding or Updating Elements
# can add a new key-value pair or update an existing one using the assignment operator '=' operator


# Adding a new key-value pair
student_ages["Anish"] = 23

# Updating an existing key-value pair
student_ages["Ram"] = 23

# print(student_ages)

#Removing Elements
# can remove a key-value pair using the del statement or the .pop() method.

# Using del
# del student_ages["ram"]  # Removes ram's entry

# Using pop
charlie_age = student_ages.pop("Anish")  # Removes Anish and returns his age

# print(student_ages)

# can remove all key-value pairs from a dictionary using the .clear() method.
student_ages.clear()  # Now student_ages is an empty dictionary


#----------------------------------------------------------------Dictionary Methods----------------------------------------------------------------
#Dictionaries have several built-in methods for common operations:

# .keys(): Returns a view object displaying a list of all the keys in the dictionary.
# .values(): Returns a view object displaying a list of all the values in the dictionary.
# .items(): Returns a view object displaying a list of all key-value pairs as tuples.
# .copy(): Creates a shallow copy of the dictionary.
#
copied_dict = mixed_dict.copy()
# print(copied_dict);
# 
# 
#  #

#------------------------------------------------------------- Iterating Through Dictionaries------------------------------------------------
# can iterate through the keys, values, or key-value pairs in a dictionary using loops.

student_ages1 = {
    "name": "Samraat",
    "age": 21,
    "is_student": True
}
# for student in student_ages1:
    # print(student)  # Prints each key (student name)

# for allValue in student_ages1.values():
    # print(allValue)  # Prints each value (student age)

# for key, value in student_ages1.items() :
    # print(f"Key: {key}   Value: {value}")  # Prints each key-value pair (student name and age)



#----------------------------------------------------------------Nested Dictionaries--------------------------------------------------------
# Dictionaries can contain other dictionaries as values, allowing you to create complex data structures.

student = {
    "Samraat": {"age": 21, "major": "Physics"},
    "Ram": {"age": 22, "major": "Biology"},
    "Sushma" : {"age" : 26, "major" : "Chemistry"},
    "Anish" : {"age" : 23, "major" : "Mathematics"}
    
}

# Accessing nested dictionary values
Samraat_major = student["Samraat"]["major"]  # to traverse through the dictionary values we need to use [] to setect the dictionary keys
# print(Samraat_major);

Ram_details = student["Ram"] # to traverse through the dictionary
# print(Ram_details);




    




