# variable declaration, number initialized
num1 = 42

# variable declaration, float initialized
num2 = 2.3

# variable declaration, boolean initialized
boolean = True

# variable declaration, string initialized
string = 'Hello World'

# variable declaration, list initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# variable declaration, dictionary initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# variable declaration, tuple initialized
fruit = ('blueberry', 'strawberry', 'banana')

# print tuple fruit, type check
print(type(fruit))

# print list [1], list / access value
print(pizza_toppings[1])

# list / value change 
pizza_toppings.append('Mushrooms')

# print dictionary ['name'], dictionary / access value
print(person['name'])

# dictionary / value change
person['name'] = 'George'

# Error: eye_color not found. dictionary / value change
person['eye_color'] = 'blue'

# print tuple [2], tuple / access value [2]
print(fruit[2])

# if / else conditional
if num1 > 45: # if conditional start, if / else conditional start
    print("It's greater") # print, if conditional end
else: # else conditional start
    print("It's lower") # else conditional end, if / else conditional end

# if / else if / else conditional
if len(string) < 5:  # if conditional start, if / else if / else conditional start
    print("It's a short word!") # print, if conditional end
elif len(string) > 15: # else if conditional start
    print("It's a long word!") # print, else if conditional end
else: # else conditional start
    print("Just right!") # print, else conditional end, if / else if / else conditional end

# for loop (from 0 to 5)
for x in range(5):
    print(x) # print variable x

# for loop (from 2 to 5)
for x in range(2,5):
    print(x) # print variable x

# for loop (from 2 to 10, incrementing by 3)
for x in range(2,10,3):
    print(x) # print variable x

# variable declaration, while loop start 
x = 0
while(x < 5): # while loop conditional
    print(x) # print variable x
    x += 1 # increment by 1
# while loop end

# list / delete value
pizza_toppings.pop()

# list / delete value [1]
pizza_toppings.pop(1)

print(person) # print dictionary
person.pop('eye_color') # Error: eye_color not found, dictionary / delete value
print(person) # print dictionary 

# for loop start
for topping in pizza_toppings:
    if topping == 'Pepperoni': # if conditional
        continue # for loop continue
    print('After 1st if statement') # print statement
    if topping == 'Olives': # if conditional
        break # for loop break
# for loop end

# function declaration
def print_hello_ten_times(): 
    for num in range(10): # for loop (from 0 to 10)
        print('Hello') # print string

# function to be called upon 
print_hello_ten_times()

# function declaration, parameter x
def print_hello_x_times(x):
    for num in range(x): # for loop until x is reached
        print('Hello') # print string

# function to be called, argument 4
print_hello_x_times(4)

# function declareation, parameter x = 10
def print_hello_x_or_ten_times(x = 10):
    for num in range(x): # for loop until 10 is reached
        print('Hello') # print string

# function to be called, no parameter
print_hello_x_or_ten_times()

# function to be called, argument 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
# All the following are comments: 

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)