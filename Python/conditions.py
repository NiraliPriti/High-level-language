score = 95
submitted_project = True
# if score  >= 90:
#     if submitted_project:
#         print("A+")
#     else: 
#         print("A")
# elif score >= 80:
#     print("B")
# else:
#     print("F")

score = 50
submitted_project = True
# if score  >= 90 and submitted_project:
#     print("A+")
# elif score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("c")
# elif score >= 60 or submitted_project:
#     print("D")
# else:
#     print("F")

# Inline if statement turnary operator
score = 70
print("A" if score>= 90 else "B" if score>= 80 else "Try Again")

#  convert coutry name in 2 form of letters
#  for flexible logic and multiple conditions
country = "USA"
if country == "United States":
    print("US")
elif country == "India":
    print("IN")
elif country == "Germany":
    print("DE")
elif country == "Egypt":
    print("EG")
else: 
    print("Unknown Coutry")

# Can be used only for matching values python 3.10+
country = "Germany"
match country:
    case "United States" | "USA":
        print("US")
    case "India":
        print("IN")
    case "Germany":
        print("DE")
    case "Egypt":
        print("EG")
    case _:
        print("Unkown Country")

# challenge 1 Python Challenge
# validate the quality and Correctness of Email Values
#  - Must Not be Empty 
#  - Must contain '.' and '@'
#  - Must contain exactly one '@' symbol
#  - Must end with '.com','.org', or '.net'
#  - Must not be longer than 254 characters
#  - Must  start and end with a letter or digit

email = "nirali@gmail.com"
print(email is not None and email != "")
print(email.__contains__('.' and '@'))
print(email.endswith(".com"or ".org"or".net"))
print(len(email)<254)
# Clean the string
email = email.strip()
valid = True
if email == "":
    print("Email cannot be empty.")
    valid = False
if not('.' in email and '@' in email):
    print("Email must contain . and @")
    valid = False
if email.count('@') != 1:
    print("Email must contain exactly one @.")
    valid = False
if not email.endswith('.com' or '.org' or '.net'):
    print("Email must end with .com .rg or .net")
    valid = False
if len(email)>254:
    print("Email must not be longer than 254 characters")
    valid = False
if not(email[0].isalnum() and email[-1].isalnum()):
    print("email must start andd end with a letter or digit")
    valid = False
if valid:
    print("Email is valid")

#  2 Python Challenge
password = "Niral i123"
# clean the password
password = password.strip()
valid = True
if password == "":
    print("Password should not be empty")
    valid = False
if not len(password)>=8:
    print("Password should contain atleast 8 characters")
    valid = False
if not any(char.islower() for char in password):
    print("password should contain at least 1 lower case")
    valid = False
if not any(char.isupper() for char in password):
    print("password must include at least 1 Upper case")
    valid = False
if password == email:
    print("Password  must not same as the email")
    valid = False
if " " in password:
    print("Password should not contain any spaces")
    valid = False
if not(password[0].isalnum and password[-1].isalnum):
    print("Password must start and end with a letter or digit")
    valid = False
if valid:
    print("Password is valid")

#  Chapter 5 Ends here Conditional Statements completed here