#  CH 3 : Numeric

x = 5
y = 5.7
z = 2 + 3j
print(type(x))
print(type(y))
print(type(z))

x = "24"
print(type(x))
x = int(x)
print(type(x))
print ( x* 3)
x = 3.24
print(int(x))
x = 3
print(float(x))

x = 3 #real
y = 4 #imaginary
print(complex(x,y))

#  Math Operators
print(2 + 3)
print( 5 -3)
print(4 * 3)
print(7 / 2)
print(7 // 2)
print(7  % 2)
print(2 ** 3)

# Assign operator
x = 2
x += 3
print(x)
x -= 3
print(x)
x *= 1
print(x)

import math
# Rounding 
print(abs(2 - 10))
price = 35.5467789
print(round(price))
print(round(price,2))
print(round(price,1))
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))
print(int(price))

import random
# print(random.random())
print(random.randint(1,6))

#  Validations
x = 7.0
print(x.is_integer())

x = 7.1
print(x.is_integer())

x = 70
print(isinstance(x, int))

y = random.randint(1, 100)
print(y)
if y % 2 == 0:
    print("number is even ", y)
else:
    print("number is odd ", y)


# ch 4 Logic and Operator
print(True)
print(False)
print(type(True))
print(bool(123))
print("Hi")
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))

email = ""
phone ="037472-2373"
username =""
# Allows registration
#if any fields is filled

# Membership operator
domain = "spam.com"
banned_domain = ["spam.com","fake.org",'bot.net']
print(domain not in banned_domain)

# identity  Operator
# is and is not
#  identity is oprator:- checks if two variables refer to the same object in memory

a = [1, 2, 3]
b = [1, 2, 3]
print( a== b)
print( a is b)

a = [1, 2, 3]
b = a
print( a== b)
print( a is b)

# 🚀Task Time :- Validate the email address it must be filled in ad not empty

email = None
print(email != None and email != "")

# None - means no value at all, it is unkown ""- means
# an empty but it is known. it is string

# Use is insted of == when checking for None


email = None
print(email is not None and email != "")

#  Challemge 
#  check if user's name is not empty and the age is greater than or equal to 18
user_name = "nirali"
age = 19
print("is username filled ?",user_name is not None and user_name != "")
print("is age is greater than or equal to 18 ? ", age>= 18)

# Challenge 2 check if the password is atleast 8 characters long and does not contain spaces
password = "   Nirali     "
password = password.replace(" ","")
print("is Password 8 character long ?", len(password)>= 8,len(password))

# challenge 2 check if user'email is not empty
# and ends with '.com'
email = ".com"
print(email.endswith('.com'),email is not None and email != "")

# challenge 4 check if username is a string, isnot none and 
# is longerr than 5 characters

user_name = "Nirali"
print(type(user_name), user_name is not None and user_name !="", len(user_name)>=5)

# challenge 5 check if user is either an admin or a moderator,
#  and either thry are not banned or they
#  have verified their email

user = "Kuchupuchhu"
admin = False
moderator = False
banned = False
email_verified = True
print(user, (admin or moderator or email_verified) and not banned  )

#  Chapetr 4 finised  🎉😎 :)
