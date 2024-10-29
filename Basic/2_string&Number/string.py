# --------------------------------------------Basic String Operations------------------------------------------------

#Concatenation
#Joining two or more strings together using the + operator.
#
str1 = "Hello"
str2 = "World"
result1 = str1 + " " + str2  # Output will be "Hello World"
print(result1);



# Repetition
# Repeating a string using the * operator.

str3 = 'samraat';
result2 = str3 * 3;  # Output will be  samraatsamraatsamraat
print( result2);

# Slicing
# Extracting a substring by specifying a start and end index.
# 

str4 = "Hello world!";
sub_str = str4[2:8];
print('The sliced String is : ', sub_str);


#Method Used for String menuplation


# .lower()                         Converts all characters in the string to lowercase.
#.upper()                          Converts all characters in the string to uppercase.
#.strip()                          Removes leading and trailing whitespace (or specified characters).
#.replace(old, new)                Replaces occurrences of a substring with another substring.
# .split(sep)                      Splits the string into a list based on a specified delimiter (default is whitespace).
# .join(iterable)                  Joins a list of strings into a single string using the specified separator.
# .find(sub)                       Returns the index of the first occurrence of a substring (returns -1 if not found).
# .count(sub)                      Counts the number of occurrences of a substring.
# .startswith(prefix)              Checks if the string starts with the specified prefix (returns True or False).
# .endswith(suffix)                 Checks if the string ends with the specified suffix.
# .capitalize()                     Capitalizes the first character of the string.
#.title()                         Capitalizes the first character of each word in the string.
# .isdigit()                     Checks if all characters in the string are digits (returns True or False).
# .isalpha()                     Checks if all characters in the string are alphabetic.
# .isalnum()                     Checks if all characters in the string are alphanumeric.
# 
#  #

upper_test = str4.upper();
print('the result is ', upper_test);



#---------------------------------------------------------------- Formatted Strings----------------------------------------------------------------

#F-Strings (Python 3.6+)
#A modern way to format strings using curly braces {}.

name = "samraat"
age = 25
city = "Nepal"

formatted_string = f"My name is {name}, I am {age} years old, and I live in {city}.";
print(formatted_string);


#str.format()
#An older method for formatting strings.
# 
# #


result = "{} is {} years old.".format(name, age)  # "Alice is 30 years old."
print(result);