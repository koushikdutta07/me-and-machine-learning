my_list = [1, 2, 3, 4, 5]

3 in my_list # Check if an element is in the list (True/ False)
10 not in my_list # Check if an element is not in the list (True/ False)
len(my_list)  # Get the number of elements in the list
my_list.append(6)  # Add an element to the end of the list
my_list.insert(2, 100)  # Insert an element at a specific index (index, element)
my_list.remove(3)  # Remove the first occurrence of an element
my_list.pop()  # Remove and return the last element
my_list.pop(0)  # Remove and return the element at a specific index
my_list.sort()  # Sort the list in ascending order
my_list.sort(reverse=True)  # Sort the list in descending order
my_list.sort(key=lambda x: -x)  # Sort the list using a custom key function
my_list.reverse()  # Reverse the order of the list
my_list.clear()  # Remove all elements from the list
my_list.extend([7, 8, 9])  # Extend the existing list by appending elements from another list
# my_list1 + my_list2  # Concatenate two lists and return a new list
# my_list1 * 3  # Repeat the list a specified number of times and return a new list
my_list.count(2)  # Count the number of occurrences of an element
my_list.index(4)  # Return the index of the first occurrence of an element
my_list.copy()  # Return a shallow copy of the list



# List slicing (start:stop:step)
my_list[1:4]  # Get a sublist from index 1 to 3
my_list[:3]  # Get a sublist from the beginning to index 2
my_list[2:]  # Get a sublist from index 2 to the end
my_list[1:4:2]  # Get a sublist from index 1 to 3 with a step of 2
my_list[::]  # Get a copy of the entire list
my_list[::2]  # Get every second element from the list
my_list[::-1]  # Get a reversed version of the list
my_list[::-2]  # Get every second element from the reversed list
my_list[::2][::-1]  # First, take every second element then reverse the list
my_list[::-1][::2]  # First, reverse the list then take every second element



# List comprehensions
squares = [x*x for x in range(5)] # create a list of squares from 0 to 4
even_numbers = [x for x in range(10) if x % 2 == 0] # create a list of even numbers from 0 to 9
