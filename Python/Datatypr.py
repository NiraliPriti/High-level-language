# Data Types
a = 10  #int
b = 3.15 # float
c = "Hello" # Str
d = 'Hi' #Str
e = "1234" # str
f = True # Boolean
g = False # Case sensitive
h = None # Nothing
i = ""  # str - blank
j = " " #Str - Empty Space


age = 18
hight = 5.6
name = "nirali"
boolean = True
status=""
print(age, type(age))
print(hight, type(hight))
print(name, type(name))
print(boolean, type(boolean))
print(status, type(status))

# str(value) :- coverts any value into string value.

print("your age is: " + str(age))
print("your age is: " , age)

# Math

# len(value) :- built in function
# return the numberr of items in a value
# return the number of characters in a string

password = "  123at790"
print(len(password))

if len(password)<8 :
    print("Your password is too short")

# Use case: validate input length
#  prevent values that are too short or too long

text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""

# count(substring):- str method output int
# return how often a word appears in the string

print(text.count("Python"))

# python is case sensitive so upper case and lower case are treated as different

# use case - detect quality issues
# count how many unwanted characters in my data


# DATA TRANSFORMATION 
# replace()

# usecase :- Clean Numeric Formats
# replace commas with dots in european -style decimal numbers

price = "1234,56"
print(price.replace(",", "."))

# replace() we can also remove unwanted parts by replacing them with an empty string("")
phone = "176-1123-56"
print(phone.replace("-","/"))

# usecase-  Clean Phone numbers
#  remove special characters from phone numbers

# chain methods  are executed in order from left to right.
#  Each replace() runs on the result of the one before it.

#  Challenge
#  Convert the messy phone number into a clean number format withonly digits

phon=" +49 (176) 123-4567"
print(phon.replace("+","00").replace(" ","")
      .replace("(","")
      .replace(")","")
      .replace("-","")
      )

#  Join String
# 'String'+'string' operator  , output : string
# join(concatinates) two strings into one.

first_name = "michel"
last_name = "scote"
last_name = first_name + " "+ last_name
print(last_name)

# usecase - build file paths
#  build dynamic paths using folder and file variables

folder = "C:/Users/Nirali"
file = "report.csv"

name = "Sam"
age = 34
is_student = False
print(f"My name is {name}, I am  {age} years old, and status is {is_student}.")

print(f" 2  + 3 = {2 + 3}")

print(f"{{This is me in curly brackets}}")

#  SPLIT 
#  Seprate date from time
# split(seprator)str method output: list of strings
# breaks a string into smaller parts

#  Breaks date into year, month and day parts

stamp1 = "2026-09-20 14:30"
print(stamp1.split(" "))
stamp = "2026-09-20 "
print(stamp.split("-"))

# Break coma-separated values into individual items

csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))

# Multiplyer 
#  Usecase -style your logs
# use repeated characters to create  clear sections in output

print("ha"*3)
print("================="*2)
# Use Case - Style Your Logs
# Use repeated 













