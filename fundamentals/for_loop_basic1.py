# 1. Basic
# print all integers from 0 to 150
for a in range(0,151): # Not sure if 150 was to be included. If not, a range of 0 to 150 would type up to 149
    print(a)

# 2. Multiples of Five
# Print all the multiples of 5 from 5 to 1,000
for b in range(5, 1005, 5): # Not sure if 1000 was to be included. If not, then just 1000 would lead up to 995
    print(b)

# 3. Counting, the Dojo Way
# Print integers 1 to 100. If divisible by 5, print "Coding" instead, If divisible by 10, print "Coding Dojo"
for c in range(1, 101):
    if (c % 10 == 0):
        c = "Coding Dojo"
    elif (c % 5 == 0):
        c = "Coding"
    print(c)

# 4. Whoa. That Sucker's Huge
# Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for d in range(1, 500001):
    if(d % 2 != 0):
        sum = sum + d
print(f"The sum of all the odd integers from 1 to 500,000 is {sum}")

# 5. Countdown by Fours
# Print positive numbers starting at 2018, counting down by fours.
for e in range(2018, 0, -4):
    print(e)

# 6. Flexible Counter 
# Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for f in range (lowNum, highNum + 1):
    if f % mult == 0:
        print(f)