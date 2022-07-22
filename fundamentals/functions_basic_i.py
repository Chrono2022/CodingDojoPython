#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

    # This will print out 5

#2
def number_of_military_branches():
    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

    # This will return an error as number_of_days_in_a_week_silicon_or_triangle_sides is not defined at all. Otherwise, if it was just military_branches, it would print 5

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

    # This will print 5, as it already returned 5, and so will not even go down to the return 10 line.

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

    # This will print 5 as since the return was already executed, the print(10) will be ignored.

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

    # If number_of_great_lakes() is called upon it would print 5, but it has no definition, so when x is equal to it, x equals nothing. 

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

    # So the first print would get an error as b and c aren't defined. The second print however is and would print (1+2) and (2+3), printing 3 and 5

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

    # Here it looks like it converts b and c to strings. 
    # In this case b is 2, and c is 5, and being converted into a string, they become "25" since they aren't added numerically

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# Here b = 100 for the first print
# Since 100 is greater than 10, we skip return 5 and go to return 10. Since we return 10, we ignore the return 7. So this should print 10. 

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

    # So if 2 < 3, which is true, we return 7. If 5 < 3, which is false, we return 14. For the 3rd, it is combined and adds up to 21.

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

    # Here we have 3 + 5 which equals 8, and so we return 8, and ignore the return 10. 

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

    # For the first print b = 500, for the function footbar b becomes 300 which is what it will print out when called upon. 
    # So we have it print in total 500, then 300, then 500 again because the last print doesn't call upon the function.

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

    # b = 500 for the first print, but now that we have a return value of 300, the second print will also say b = 300.
    # The last print will say 500 since footbar() is not technically called upon for it.

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

    # b = 500, then b becomes 300, which it will print for the next 2 printings. 

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

    # function foo() calls for print(1), bar(), and print(2), then bar becomes defined as print(3)
    # So when foo() is called again we have bar as 3, so it will print 1, 3, and 2. 

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

    # Here foo() prints 1, prints x which equals bar(), and we get a return of 10.
    # bar() becomes defined as 3 with a return of 5
    # When y calls foo(), foo() prints 1, then x which equals bar which prints 3, then bar returns 5, printing 1, 3, and 5
    # When y is printed, and y = foo(), foo() returns 10, printing 10. 