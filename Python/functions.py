# Functions
#  reusable block of code
# def function_name():
    # line of code
#  function_name()  Function call

def make_coffee():
    print("Start Machine")
    print("make cofee")
    print("Add Milk")
    print("Enjoye it")



print("Wake up")
make_coffee()
print("working for a while ")
make_coffee()

# Function organize and structure our code and make our life easier

# Built in Function (Just Calling)
print(len("Python"))

import math
# Function from libraries
number = 4.2
print(math.ceil(number))


# User defined function
def greet():
    print("Hello")
greet()

# Parameters and arguments
# function shape

def multiple_two(x):  #Parameter
    print(x*2)

multiple_two(3)   #Argument

case_rule = "n/a"
def clean_name(name):  #Parameter
    cleaned = name.strip().lower()  # Local
    if case_rule == "lower":
        cleaned = cleaned.lower()
    print(cleaned)

clean_name("  KuchhuPuchhu  ")
clean_name(" harsHi")
print("The Rule is:", case_rule)
# Pass Data in:- pass the value as a parameter to handle any input
# Normalize Strings:- remove extra spaces and make text lowercase

def new_name(first_name, last_name, Country= "n/a"):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name =first + " " + last
    print(full_name, "From", Country)

new_name("NiraLi ", " FrootY ", "IN")  #Postinal
# Rule For Postional Argument:- 
#  The Order of Arguments must match the order of the Parameters
# Keyword Arguments
new_name(first_name = "Nirali ", last_name = "ferootY", Country = "IN")

# Mixed Arguments
new_name(" NiRali ", last_name = " Khalas ", Country="IN")

# Default Parameter
new_name("Nisha ","Aura ")

# *args ** kwargs
# Allows functions to accept a unknown of arguments

# * Positional arguments
# ** Keyword arguments
#  Calc the total of values
def total(*args):
    print(sum(args))

total(1,2)
total(1,3,4,4,5,56,)

# Create a the user profile
def create_user(**kwargs):
    print(type(kwargs))
    print(kwargs)

create_user(first_name = "Nirali",
            last_name = "Khalas",
            age=33,
            country= "Egypt")

create_user(name="Ronaldo",
            country="Portugal")

# ** works only with keyword arguments

# *args :- positional rguments, only values,same type of defination store data as a tuple(1,2)

#  **kwargs :- keywords arguments, "names and values", Different types of information stores data asa dictionary  { "name": "neha"}

# Return 
def new_name(name):
    if not name:
        return None
    else:
        cleaned = name.strip().lower()
        return cleaned

cln_name = new_name(" NIrAli ")
print(cln_name)

# If a function has no return statement, python returns None

def new_name(name):
        lo_cleaned = name.strip().lower()
        up_cleaned = name.strip().upper()
        return lo_cleaned, up_cleaned

cln_name = new_name(" NIrAli ")
print(cln_name)
print(type(cln_name))
lo_name, up_name = new_name(" VinAyak ")
print(lo_name)
print(up_name)

# Action function 

#  Store application log messages in a file whenerverr an event occurs
def write_log(message):
    with open(r"C:\Users\neha1\Learning\SQL_learning\Python\app.log","a") as file:
        file.write(message + "\n")

# write_log("App Started")
# write_log("User Logged in")
# write_log("App Stopped")

# Transformation function

# Task:- cleans email addresses and split them into structured data (username and domain)

email = "nirali@gmail.com"
print(email)
username = email.split('@')
print(username)
print(type(username))
print("Username : ", username[0])
print("Domain : ", username[1])

def clean_and_split(email):
    cl_email = email.strip().lower()
    username,domain = cl_email.split("@")
    return {"username":  username,
            "domain": domain}
print(clean_and_split("quetee@gmail.com"))

# Validation Function
#  Checks whether the password meets the minimum requirement of 8 characters
def is_valid_password(password):
    return len(password) >= 8

print(is_valid_password("nirali123456"))

# Check whether an email has a basic valid format.
def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email("nirali@123.in"))

# Orchestrator function
#  Control program flow by calling other functions in the correct order.

# 1 Recieve an email from the user
# 2 Validate the email
# 3 if it is invalid, log an error in a file
# 4 if it is valid, clean and structure the email.
# 5 log each step of the program.


# Orchestrator function
def process_user_email(email):
    write_log("App Started")

    if not is_valid_email(email):
        write_log(f"Invalid Email recived: {email}")
    else:
        clean_email = clean_and_split(email)
        write_log(f"Processed Email: {clean_email}")
    write_log("App Stopped")

# email = input("Please Entern  your Email : " )
# process_user_email(email)

# Function Styling tips :
# 1 Use snack_case for function Names:
# write function names in lowercase and seprate words with underscores

# Use clear decriptive function names
# - describe exactly what the function does
# - start with a verb
# - Use full words, avoid abbreviations

# 3 parameter names full names describe their values
# - use full, meaningful words
# - avoid abbreviation and single letters

def calculate_discount(price : float,rate: float)-> float:
# 4 always describe functions using docstring
# - help teammate to understand your code

    """Calculate the final price after paying a discount
    Args:
        price (float): original product price
        rate (float): Discount rate as a numbers e.g 20 for 20%
    Returns :
    final_price(float): final price after applying discount
    """

    final_price = price - (price *rate/100)
    return final_price
# """""":- docstring
# Python store it inside the function and can be reused by tools, editors ...
help(calculate_discount)
# 5 Replace print with return to send data back to the programm
# 6 Dom't change parameter values directly,create local variable for any processing.

# 7 use data type hints 
# always add type hints to parameters and return to make the function easier to understand
calculate_discount(100,20)