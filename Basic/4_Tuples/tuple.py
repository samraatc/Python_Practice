# Creating Tuples
#A tuple is created by enclosing items in parentheses (), separated by commas. 
# If a tuple has only one item, you need to add a comma after the item to differentiate it from a regular expression enclosed in parentheses.

# Empty tuple
empty_tuple = ()

# Tuple with integers
numbers = (1, 2, 3)

# Tuple with mixed data types
mixed_tuple = (1, "hello", 3.5, True)

# Single-item tuple
single_item_tuple = (1,)  # Note the comma

print(mixed_tuple);

if "hello" in mixed_tuple:      # to test the value is present in the tuple or not
    print("hello found in tuple")


# Tuples are indexed similarly to lists, allowing access to individual elements using their index.

numbers = (10, 20, 30, 40, 50)
first_element = numbers[0]  # 10
last_element = numbers[-1]   # 50


# all the opertion can be perform as list 
# but list are mutable and tuple are immutable

# numbers[1] = 22;    # This will give TypeError: 'tuple' object does not support item assignmen
# print(numbers);




