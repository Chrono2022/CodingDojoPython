# 1. Countdown

# Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(a):
    return list(range(a,-1,-1))
countdown(5)

# 2. Print and Return

# Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_and_return(b):
    x = b[0]
    y = b[1]
    print(x)
    return y
print_and_return([1,2])

# 3. First Plus Length

# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def first_plus_length(c):
    a = len(c)
    b = c[0]
    return a + b
first_plus_length([1,2,3,4,5])

# 4. Vales Greater than Second

# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    newlist = []
    for value in list:
        if value > list[1]:
            newlist.append(value)
    return newlist
values_greater_than_second([5,2,3,2,1,4])

# 5. This length, that value

# Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value(length, value):
    newList = []
    for loop in range(length):
        newList.append(value)
    return newList
length_and_value(4,7)