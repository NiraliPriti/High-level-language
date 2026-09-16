#  Create Lists
empty = []
letters = ['a','b','c']
numbers = [1, 2, 3]
mixed = [1, 'a', True, None]
print(mixed)
print(type(mixed))

letters = list('Python')
print(letters)

numbers =  list(range(5))
print(numbers)

matrix = [['a', 'b','c'], ['d','e','f']]
print(matrix)
print(type(matrix))

mixed_matrix = [['a','b'],
                [1, 2, 3],
                [True]]
print(mixed_matrix)
print(type(mixed_matrix))
#  we can mix data types in the same list
# Nested Matrix 

# Read And Access
lst = ['a','b','c','d']
print(lst)
print(lst[0])
print(lst[-1])

# Nested Matrix
matrix = [['a', 'b','c'], 
          ['d','e','f'],
          ['g','h','i']
          ]
print(matrix)
print(matrix[-1])
print(matrix[1][1])
print(matrix[:2]) #slicing
print(matrix[1:])
print(matrix[2][:2])
# For matrix first go with row then column
lst = [ 'a','b','c','d']
print(lst)
print(lst[0])
print(lst[:2]) # Slicing
print(lst[2:])
print(lst[:])

# Unpacking list

person = ['Ganesha',29,'Data Engineer','city','Spain']
# name = person[0]
# age = person[1]
# role = person[2]
# country = person[3]

# Unpacking is clean, easy and make code simple to extend
# name,age,role,country = person
# name,*details,country = person
# name,*details = person
*details,city,country = person

# print(name)
print(details)
print(city)

# Only one asterisk * is allowed in unpacking

# Unpacking rules
#  no of variables must match the values exactly -- not less not more

# numbers = [1, 2, 3 ,4 ,5]
# first, second, third , fourth = numbers

# * asterisk collect leftovers, and it is fine if there are none
numbers = [1]
first , *rest = numbers
print(first)
print(rest)

numbers = 'Hi'
first , *rest = numbers
print(first)
print(rest)
# we can unpack any sequence (list, tuples, strings, etc.)

# '_'
person = ['Ganesha',29,'Data Engineer','Spain']

name, *_, country = person

print(name)
print(country)

# *Astrisk  store the rest in new list
#  _ underscore skips items


#  Explore and analysis Lists
numbers = [1, 5, 4, 3, 2, 5]
print("Max: ",max(numbers)) # Highest  value
print("Min: ", min(numbers)) #lowest
print("Sum: ",sum(numbers))
print("Length: ",len(numbers))

#  all all items are true?
print("All: ", all(numbers))
print("All: ", all([1, 0, 2]))
print("All: ", all(['a', '', 'b']))
print("All: ", all(['a', 'c', 'b']))

print("any:  ",any(numbers))
print("any:  ",any([1, 0, 2]))
print("any : ",any(['a', '', 'b']))
print("any:  ",any(['a', 'c', 'b']))
print("any: ", any([0,0,0]) )

# count : how many times a value in appears in the list
print("Count: ",numbers.count(5))

#  index(b): return the postion of the first occurance of a value
print("Index: ", numbers.index(5))

#  in oprator checks if a value exists in a list
list1 = [1, 2, 3]
list2 = [1,2,3]
print(list1 is list2)

#  Changing list add items
#  append the new value at the end
letters = [ 'a', 'b','c']
letters.append('x')
letters.append('y')

# Inser at a specification
letters.insert(0, 'x')
letters.insert(3,'y')
print(letters)

matrix = [['a', 'b','c'], 
          ['d','e','f'],
          ['g','h','i']
          ]
matrix. append(['x','y','z'])
matrix.insert(0,['a','a','a'])
matrix[1].append('x')
matrix[0].insert(0,'z')
print(matrix)

#  Remove items 
#  by value -> remove('b')
#  by postion-> pop():-> default remove last item
# pop will remove items an return it
lettrs = ['a', 'b','a']
lettrs.remove('a')  # this remove first a
lettrs.remove('a') # this remove second  a 
print(lettrs)

char = ['a','b','c']
removed = char.pop(1)
print(removed)
print(char)

matrix = [['a', 'b','c'], 
          ['d','e','f'],
          ['g','h','i']
          ]

# matrix.remove(['a','b','c'])
# matrix.pop()
matrix[1].remove('e')
# matrix[2].remove('g')
matrix[-1].pop(0)
matrix[0].pop() #by default it will remove last item
# matrix[0].remove('c')
print(matrix)

# clear() remove all items
# .remove(value): remove by value(firstmatch)
# pop(index) remove return by position
# default last item

# Update data 
letters = ['a','b','c']
letters[0] = 'x'
letters[1] = 'y'
letters = 'z'
print(letters)
print(type(letters))

# Update the content of the last list
matrix= [
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
]
matrix[-1] = ['x','y','z']
matrix[0][0] = '-'
matrix[1][1] = '-'
matrix[2][2] = '-'
print(matrix)

# Sorting List
letters = ['c','a','b']
letters.sort(reverse = True)

print(letters)

matrix= [
    ['d','e','f'],
    ['a','z','i'],
    ['a','a','c']
]
matrix[1].sort()
print(matrix)

# Sorts by the first item of each list
# Task sort the data without changing the original list

new_list = sorted(letters, reverse = True  )
print('Original List: ',letters)
print('Sorted list: ', new_list)

letters = ['c','a','b']
new_list = list(reversed(letters))
print('Original list : ',letters)
print('reversed list object: ', reversed(letters))
print('Reversed list', new_list)

# Reversed() creates an iterator object, not a list
# Copy list

# Create a copy of the list in a new variable
letters = ['a','b','c']
letters_copy = letters
letters.pop()
letters_copy.append('z')
print('Original: ', letters)
print('Copy: ', letters_copy)
# Both the variables reference the same list in memory

# Shallow copy
letters = ['a','b','c']
letters_copy = letters.copy()
letters.pop()
letters_copy.append('z')
print('Original: ', letters)
print('Copy: ', letters_copy)
#  Copy creates a seprate list in memory


matrix= [
    ['a','b'],
    ['d','e'],
]
matrix_copy = matrix.copy()
matrix.pop()
matrix_copy[0].append('z')
print('Original: ', matrix)
print('Copy: ', matrix_copy)
# The copy() method creates a shallow copy


import copy
matrix= [
    ['a','b'],
    ['d','e'],
]
matrix_copy = copy.deepcopy(matrix)
matrix.pop()
matrix_copy[0].append('z')
print('Original: ', matrix)
print('Copy: ', matrix_copy)
# Copy.deep copy() creates a true, independent copy for all levels
matrix_copy = copy.copy(matrix)
print('Original: ', matrix)
print('Copy: ', matrix_copy)
# Copy.copy() creates a shallow copy just like the method copy()
# Copy.copy() is more general than list.copy(), not limited to lists


# Testing is operator
# Checks if two variables refer to the same object

import copy

original = [
    ['a','b'],
    ['c','d']
]

# Assignment
copy1 = original 
print("Same object ? ",original is copy1 ,"\n")

# Shallow copy
copy2  = original.copy()
print("Same Object?", original is copy2)
print("Shared Lists ?",original[0] is copy2[0],"\n")
# Deep Copy 
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3)
print("Shared Lists ?",original[0] is copy3[0],"\n")

# Tips:- Use the is operator to check if the coppies are truely independent

# Combining
letters = ['a','b','c']
numbers = [1, 2 ,3]
comb = letters + numbers
print(comb)
comb = [letters, numbers]
print(comb)
# * Multiple Operator
print(letters * 2)
# Extends does not create a new list; it expands the original one.
letters = ['a','b','c']
numbers = [1, 2, 3]
numbers.extend(letters)
print(letters)
print(numbers)
# zip()
letters = ['a','b','c']
numbers = [1, 2, 3.4]
comb = list(zip(letters, numbers,"Hi"))
print(comb)

id = [101, 102, 103]
names = ['Ali','Sara','John']
# Pair customers with their IDs (rebuild the relationship)
comb = list(zip(id,names))
print(comb)

# Iterators
letters = ['a','b','c']
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)

#  we use iteration to transform data
# tore the transfformed results in new list

# enumerator 
letters = ['a',' ','c']

for index, value in enumerate(letters):
    print(index, value)

# ENumerate Use Case: find the e\exact position of the bad data in your list

# Reversed an iterator that flips the data order

letters = ['a','b','c']
print(list(reversed(letters)))
for l in reversed(letters):
    print(l)

# Zip Combines two or more sequence into pairs(tuples)
letters = ['a','b','c']
numbers = [1,2,3]
print(list(zip(letters, numbers)))
for l, n in zip(letters, numbers):
    print(l,n)

# iterator map
letters = ['a','b','c']
print(list(map(str.upper,letters)))

numbers = ['1','2','3']
print((list(map(int, numbers))))

# Clean up the list by removing alll unwanted spaces

names = [ ' Maria ', ' John ','  Kumar']
print((list(map(str.strip,names))))
for n in map(str.strip, names):
    print(n)
# Map is fast, clean way to do data transformation

# Filter
letters = ['a','','b',None,'c',False]
# Clean up the list by removing unvalid data
# None:- remove all falsy values like 0,"", or False
print(list(filter(None, letters)))
# bool works the same it filters out all falsy values
print(list(filter(bool, letters)))

items = ['sql','123','python','42']
# keeps only letters items
# print(list(filter(str.isalpha,items)))
for i in filter(str.isalpha,items):
    print(i)

# filter() is perfect for cleaning up data in your structure

# Lambda 
multiple = lambda x: x*2
print(multiple(2))

add = lambda x, y : x + y
print(add(1,2))

check = lambda i: i in "python"
print(check('n'))

# lambda + map
prices = ['$12.50','$9.99','$100.00']
print(list(map(lambda p: float(p.replace('$','')),prices)))

prices = [120,30,300, 80]
# remove all prices lower than 100
print(list(filter(lambda p:p>=100,prices)))

students = [['Maria', 60],
            ['Nirali', 90],
            ['harsh', 100]]
print(list(filter(lambda row : row[1]>70,students)))

# Challenge 1 
# Keeps only students with names starting with 'M'

students = [['Mummy', 100],
            ['chintu',90],
            ['Motu', 56]
            ]

print(list(filter(lambda row: row[0].startswith('M'), students )))

# List Comprehensions
domains = ['www.google.com',
           'openai.com',
           'localhost',
           'www.DATAwithNirali.com']

# Normalize the domain into standard format
cleaned = [
    # Data Transformation
    d.lower().replace('www.','')
    # For loop
    for d in domains
    # Data Filtering
    if '.' in d
]
print(cleaned)

# list is orderd allow duplicates and index

my_tuple = (10,30, 40, 10)
print(my_tuple) #ordered # allow duplicates 
print(my_tuple[1]) # Indexed
# my_tuple[3] = 40    immutable

print(sorted(my_tuple))

my_set = { 10, 20, 30, 5, 10}
print(my_set)   #Unordered
# remove duplicates
# print(my_set[0])Not indexed
my_set.remove(20)
print(my_set)#mutables

#  set methods

a = { 10, 20, 30, 40}

a.add(50)
print(a)
# add() insert the items somewhere in the set, but only if it is new
# update()
# merges anpther group of values into the set 
# a.update({1,2})
# print(a)
# we can use math operators as quick shortcuts : | & - ^
a |= {1,2}
print(a)
# a.remove(10) # remove the value if it exist if element not exist it will give error
print(a)
# discard() :- remove the items if it exists and does nothing if it does not 
a.discard(100)
# a.pop() # pop will remove something totaly random value
print(a)

# Set with Math
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
# Mathematical Operation
print(a.union(b))
#  Math operators return a new set and leave the originals untouched
print( a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)
print(b - a)

print(a.symmetric_difference(b))
print( a ^ b)

#  Relationship Management
a = {10, 20}
b = {30, 40, 50, 60}
# Returns true if  All items in this set exist in the other
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(b))

#  Dicstionaries
my_dict = {
    'a': 10,
    'b':20,
    'c':20,
    'a':40
}
print(my_dict) #Ordered
# Keys are unique
# Values alllow duplicates
print(my_dict['b']) #Not indexed
#  we access values by using their keys ,not indexes.
my_dict['c'] = 80
print(my_dict)
# mutable

user = {"id":1,"age":30,"city":'berlin'}
print(user["city"])
# if the key is not found python throws a key error
# give()  return value safely, gives None if missing or your defalt values.
print(user.get("name","unknown"))


# Check
print("age" in user )
print("name" not in user )

# View 
# Gives you live view of the dictionary's keys, values or key value pairs
print(user.keys())
# keys() return all the keys in your dictionary

print(user.values())
print(user.items())

# Looping
for key, values in user.items():
    print(key, values)


# Add, remove Update
user["name"] = "John"#Add
user["age"] = 35  #Update
user.update({"age": 40,"city": 'paris'})
print(user)

age = user.pop("salary", "not found")
print(user)
print("Removed item: ", age)

user.popitem()
print(user)

user = {"id":None,
        "age":None,
        "city":None
        }
user = dict.fromkeys(["id","name","age","city"],None)
print(user)
# builds a new dictionary where all keys get the same default values

users = {"id": 1,"name":"ganesha","age":10,"city":"nirali house"}

user_str = {
    k: v.upper() #Expression
    for k, v in users.items() # loop
    if isinstance(v, str) # Filter
}

print(user_str)

# Data Structure finished here :)