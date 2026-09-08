# Interview Questions for Python developer interview
# List :- a collection of ordered items.
my_list = [ 1, 2, 3, 4, 5]
print(my_list)
mixed = ["abc", 34, True]
print(mixed)

#  tuple example
fruits = ("apple", "banana", "cherry", 4.5546456)
print(fruits)

# Main difference between list and tuple 
#  list is mutable while tuples are immutable.
my_list = ["apple", "banana"]
my_list[0] = "cherry"
my_list.append("orange")
print(my_list)

# --- TUPLE EXAMPLE ---
my_tuple = ("apple", "banana")
# my_tuple[0] = "cherry"  --> Throws a TypeError
# my_tuple.append("orange") --> Throws an AttributeError

# What are List Comprehensions? 
# Simple Answer for the Interview: "List comprehension is a shorter, cleaner way to create a new list from an existing list or iterable using just a single line of code. It replaces traditional for loops."

numbers = [ 1, 2, 3, 4, 5]
squares = []
# for x in numbers:
    # squares.append(x)
squares = [x *x for x in numbers]

print(squares)

#  What is the difference between is and == in Python?Simple Answer for the Interview: "== checks if the values of two variables are equal. On the other hand, is checks if both variables point to the exact same object in memory."Deep Concept Explanation: Think of it like identical twin brothers. They look exactly the same (their "value" is equal, so == is True). However, they are still two separate human beings living in two different bodies (their memory address is different, so is is False).

list_a = [1, 2, 3]
list_b = [1, 2, 3]
print(list_a == list_b) # True values are identical
print( list_a is list_b)  # False they live in different memory.

#  What is an ORM (Object-Relational Mapping)?
# Simple Answer for the Interview: 
# "An ORM is a programming technique that lets you interact with a database using Python code (like objects and classes) instead of writing raw SQL queries."

# Slicing syntax works as string[start:stop:step]. Leaving start and stop blank tells Python to look at the entire string. Setting the step to -1 tells Python to read from right to left instead of left to right. It is the fastest and most readable way to reverse a string in Python.

# How do you check if a word is a Palindrome (reads the same backward as forward) in Python

def is_palindrome(word):
    # word = word.lower()
    return word == word[::-1]

print(is_palindrome("radaR"))
print(is_palindrome("python"))

# remove() removes an element by value.
numbers = [10, 20, 30]
y = numbers.remove(20)
print(numbers)
print(y)

# pop() remove an element  by index and returns it.
numbers_1 = [10, 20, 30]

x = numbers_1.pop(1)
print(numbers_1)
print(x)


numbers = [10, 20, 30]

del numbers[1]

x = 'abcd'
for i in range(len(x)):  
    print(i, end= " ")
