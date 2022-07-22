# 1. Update Values in Dictionaries and Lists:

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1a. Change the val;ue 10 in x to 15:

def changeNumber():
    x[1][0] = 15
    return list
changeNumber()

# 1b. Change the last_name of the first student from 'Jordan' to 'Bryant':

def changeLastName():
    students[0]['last_name'] = 'Bryant'
    return students
changeLastName()

# 1c. In the sports_directory, change 'Messi' to 'Andres'

def changeSportsName():
    sports_directory['soccer'][0] = 'Andres'
    return sports_directory
changeSportsName()

# 1d. Change the value 20 in z to 30

def changeValue():
    z[0]['y'] = 30
    return z
changeValue()

# 2. Iterate Through a List of Dictionaries

# Given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range(len(students)):
        print('first_name - ' + students[i]['first_name'] + ', ' + 'last_name - ' + students[i]['last_name'])
iterateDictionary(students)

# 3. Get Values From a List of Dictionaries

# Given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.

def iterateDictionary2(key_name, some_list):
    for a in range(len(some_list)):
        print(some_list[a][key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4. Iterate Through a Dictionary With List Values

# Given a dictionary whose values are all lists, prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list. 

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dict):
    for key,val in dict.items():
        print("")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])
print_info(dojo)


def printInfo(some_dict):
    for a in some_dict:
        print(len(some_dict[a]), a.upper())
        for b in range(len(some_dict[a])):
            print(some_dict[a][b])
        print("")
printInfo(dojo)
