# # A list is created by enclosing items in square brackets [], separated by commas.

# # empty lists are
# my_list = [];

# # Mixed lists are
# MixedList = [1, 2, 'Three', 'Four', 'Five', 4.5, True, False ];

# #List of lists(nested list)
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];



# #You can access elements in a list by their index. Python lists are zero-indexed, meaning the first element is at index 0.

# numbers = [10, 20, 30, 40, 50]
# first_element = numbers[0]  # 10
# last_element = numbers[-1]  # 50

# print(first_element, last_element);


# #Slicing lets you access a range of elements within a list by specifying a start and end index

# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
# sub_list = num[3:7]; 
# print(sub_list);    # the last index is not included



# #Lists are mutable, so you can modify elements, add new items, or remove existing items
# #You can change the value of an element by assigning a new value to a specific index.

# # numbers[0] = 5;
# # print(numbers);  # [5, 20, 30, 40, 50]

# number = [5, 20, 30, 40, 50];
# number[2] = 60;  # change the value of the third element from 30 to 60
# print(number); # 5, 20, 30, 40, 50



# #You can also add new items to the list using the append() method.
# number.append(60)
# print(number);   # append() method add new items to the last/end of list element



# # You can remove items from the list using the remove() method.


# number.remove(20);



# # insert(index, x): Inserts an item at a specific index.

# number.insert(1, 10);
# print(number);   # insert() method inserts new items at a specific index and rest of the element in the list shift to the next index value


# #extend(iterable): Adds all elements from an iterable (like another list) to the end of the list.

# numbers.extend([100, 200, 300]);
# print(numbers);   # extend() method add all items from another list to the end of the list


# # You can concatenate lists using the + operator.
# number.extend(numbers);
# print(number);   # extend() method add all items from another list to the end of the list




# # You can check if an item is in a list using the in keyword.

# print(10 in numbers);  # True
# print(100 in numbers);  # False


# # pop(index): Removes and returns the item at the specified index (defaults to the last item if no index is given).

# popped_item = number.pop(10);   # if no index is given then returns the end item/element of list
# print(popped_item);  # pop() method removes an item from the list and returns it


# #clear(): Removes all items from the list.

# # number.clear();
# # numbers.clear();
# # print(number);  # clear() method removes all items from the list
# # print(numbers);  # clear() method removes all items from the list




# #----------------------------------------------------------------List Methods for Sorting and Reversing----------------------------------------------------------------


# #Sorting 
# #sort(): Sorts the list in place (modifies the original list). You can use the reverse=True parameter to sort in descending order.


# # numbers.sort(reverse=True);
# numbers1 = [40, 10, 30, 20, 10]
# print(numbers1);  # [40, 10, 30, 20]
# numbers1.sort()  # [10, 20, 30, 40]  after sorting the output is sorted
# print(numbers1);  # [10, 20, 30, 40]


# # sorted(list_name, reverse=True) for the reversing order of numbers in llist
# sorted_numbers = sorted(numbers1, reverse=True)  # [40, 30, 20, 10]
# print(sorted_numbers);    # this will reverse the order of numbers 


# Or you can do 
# numbers1.reverse()
# print(numbers1);  # [40, 30, 20, 10]  after reversing the output 

 #reversed(list): Returns an iterator that yields the elements in reverse order.
# reversed_numbers = list(reversed(numbers1));



#index(x): Returns the index of the first occurrence of x.

# index_of_30 = numbers1.index(20) 
# print(index_of_30);  # 



# #count(x): Returns the count of occurrences of x in the list.

# count_of_10 = numbers1.count(10)  # 1
# print(count_of_10);



# copy(): Creates a shallow copy of the list.
# copy_num = numbers1.copy();     # copy() returns a shallow copy of the list it allocate different memory space, but when values are assigned for one variable to other than the memory allocated are same
# print(copy_num);
# copy_num_var = numbers1;
# print(copy_num_var);   # this will print same memory location as numbers1, hence changes in copy_num_var will reflect in numbers1 as well


# Use append() to add an item to the end and pop() to remove the last item.  Use append() to add an item to the end and pop(0) to remove the first item.

numTest = [1, 2, 3, 4, 5];
numTest.append(6);
print(numTest);  # [1, 2, 3, 4, 5, 6]
# numTest.pop();   
# numTest.pop()
# print(numTest);  # [1, 2, 3, 4]   ## This will perform as last in First Out (LIFO)


# But

numTest.pop(0);
numTest.pop(0);
print(numTest);    ## This will perform as First in First Out (FIFO)





