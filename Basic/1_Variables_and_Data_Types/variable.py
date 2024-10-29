# what is variable :- A variable is a name that refers to a value stored in memory, we can use any name to assign the variable. variable declearation have some specific rules to be flow 

#Names can include: Letters (a-z, A-Z), numbers (0-9), and underscores (_).
#Names must start with: A letter or an underscore, not a number.
#No special characters: Avoid symbols like @, $, %, etc.
#Case-sensitive: myVariable and myvariable are different.


#  Data Types in Python
# Numeric Types:- int, float, complex...
# String 
# Boolean 
# Sequence Types  :- list, tuple, range...
# Mapping Type :- dictionary...
# Set Types :- set, frozenset...
#    

# Practice 
# Create a variable named Use the type() function to check the types of the variables you have created. Create a string variable named greeting and assign it the value "Hello, World!".
# A.Print the length of the string.
# B.Convert the string to uppercase and print it

# example Of data type 
age = 25        # An integer
name = "Alice"  # A string
height = 5.6    # A float
is_student = True  # A boolean


# Step 1: Variable Creation
# Creating variables for two numbers

num1 = 10        # First number (integer)
num2 = 5         # Second number (integer)

# Step 2: Perform Arithmetic Operations
# Performing operations
addition = num1 + num2           # Addition
subtraction = num1 - num2        # Subtraction
multiplication = num1 * num2     # Multiplication
division = num1 / num2           # Division

# Step 3: Print Results
print("Addition:", addition)            # Output: Addition: 15
print("Subtraction:", subtraction)      # Output: Subtraction: 5
print("Multiplication:", multiplication) # Output: Multiplication: 50
print("Division:", division)             # Output: Division: 2.0


# type() to check the type of data present in variable
# 
DataType_test = type(addition);
print("The data type of this variable is ", DataType_test);


# A.Print the length of the string.
length_of_string = len(name);
print('The lengthe Of given String is ', length_of_string);


# B.Convert the string to uppercase and print it
String_to_upperCase = name.upper();
print('The upper Case of given string is ', String_to_upperCase); 



# we can assign variable like :-  x, y, z = 1, 2, 3  
# a = b = c = 100

# ---------------------------------------------------Advanced Data Types-------------------------------------------

# List or we can say it as Array in Python

# syntax :-  Variable_Name = [Values seperated with comma]  eg

my_List_test = [1, 2, 3, 4, 5, 6, 7, 8, 9];
print('List is : ', my_List_test);



# Tuple
# syntax :-  Variavle_Name = (Value seperated with comma) eg

My_Tuple_test = (1, 2, 3, 4, 5);
print('The given Tuple is : ',My_Tuple_test);


# Dictionary
# syntax :-  Variable_Name = {Values are in key value pairs and  seperated with comma}  eg 

My_Dictionary_test = {
    'age' : 25,   
    'name' : "Alice",  
    'height' : 5.6  
};

print('The Dictionary is ', My_Dictionary_test);
