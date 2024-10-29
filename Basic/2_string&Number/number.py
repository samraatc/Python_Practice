

#----------------------------------------------Common Functions for Number Manipulation--------------------------------------

#Absolute Value
#abs(x): Returns the absolute value of a number

result1 = abs(-10)  #  output will be 10
print(result1);



# Rounding
# round(x, n): Rounds a number to n decimal places (default is 0).

result2 = round(3.14159, 2)  #  output will be 3.14
print(result2);


# Power
# pow(x, y): Raises x to the power of y

result3 = pow(2, 3)  # 8
print(result3);


#Maximum and Minimum
#max(x1, x2, ...): Returns the largest value.
#min(x1, x2, ...): Returns the smallest value

result4 = max(10, 5, 20, 3)  # 20
print(result4);
result5 = min(10, 5, 20, 3)  # 3
print(result5);



#----------------------------------------------------------------Math Module for Advanced Manipulations----------------------------------------------------------------

import math


# Square Root
#math.sqrt(x): Returns the square root of x

result_sqrt = math.sqrt(16)  # 4.0
print(result_sqrt);


# Factorial
# math.factorial(x): Returns the factorial of an integer x

result_fraction = math.factorial( 5 );
print(result_fraction);  


###
#Constants
#math.pi: The mathematical constant π (~3.14159).
#math.e: The mathematical constant e (~2.71828)

pi_value = math.pi
e_value = math.e
print('The value of pi is :', pi_value);
print('The value of e is :', e_value);


# Trigonometric Functions
# math.sin(x), math.cos(x), math.tan(x): Calculates sine, cosine, and tangent of x (in radians).

result_trig = math.sin(math.pi / 2)  # 1.0
print(result_trig);


# Logarithmic Functions
# math.log(x): Returns the natural logarithm (base e) of x.
# math.log10(x): Returns the logarithm of x to base 10


result_log = math.log(10)  # ~2.302
print (result_log);



#----------------------------------------------------------------Working with Random Numbers----------------------------------------------------------------

import random



#random.randint(a, b): Returns a random integer between a and b.

random_int = random.randint(1, 10)  # Random integer between 1 and 100
print(random_int);


#random.random(): Returns a random floating point number between 0 and 1.
result_random = random.random()  # Random float between 0 and 1
print(result_random);


#random.choice(sequence): Returns a random element from a non-empty sequence like List 

choices = [10, 20, 30, 40]
result_choice = random.choice(choices)  # Randomly selects an item from the list
print(result_choice);













