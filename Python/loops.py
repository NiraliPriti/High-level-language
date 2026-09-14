#  Chapter 6 Loops in python
# for i in (1,2,3,4,5):
#     print(f"Round: {i}")

items = " Python"
for item in items:
    print(f"Round: {item}")

for item in range(2, 10, 2):
    print(f"Round: {item}")

scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
    print("Current total:",total)
print("Final Total:", total)

# we use for loops to transform data 
# like cleaning before processing
files = [' Report.csv', 'DATA.csv ', ' final.csv']
for file in files:
    file = file.strip().lower().replace('.txt','.csv')
    print(f"Processing {file}")

# Challenge 1 
# Print the 7 times table from 1 to 10 using a for loop
for i in range (1,11):
    print(f" 7 X {i} = ", 7*i)

# Challenge 2 print following pattern
# print a left - aligned pyramid of stars with 6 rows using a for loop
# *
# **
# ***
# ****
# *****
rows = 6
for i in range(1,rows +1):
    for j in range(1, i+1):
        print("*",end=" ")
    print()

# Advanced loops
#  Breaks it stops immidietly
names = [ 'john','maria','','kumar']
for name in names:
    if name == '':
        print('Empty value detected')
        break
    print(f'Name = {name}')
# Continue : it skips one loop cycle without stopping the loop
# skip one and go
names = [ 'john','maria','','kumar']
for name in names:
    if name == '':
        print('Empty value detected')
        continue
    print(f'Name = {name}')
# Pass it is a placeholder where nothing happens
#  For now do nothing just pass
names = [ 'john','maria','','kumar']
for name in names:
    if name == '':
        print('Empty value detected')
        name = name.replace('','unknown')
        pass # to do : Handle empty value
    print(f'Name = {name}')
#  Task :- Loop through a list of days and print only the working days skipping the weekends
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for day in days:
    if day == "Sunday"or day == "Saturday":
        continue
    print(f"Working days {day}")

weekends = ["Sunday","Saturday"]
for day in days:
    if day in weekends:
        continue
    print(f"Working days {day}")
# Task 2 Scan emails to blocks unsafe data from entering your system
emails = [
    'neha@123.com',
    'neha@gmail.com',
    'DROP TABLE USERS;'
    'nirali@priti.net',
    'neha#harsh.in'
]
for email in emails:
    if ';' in email:
        print('SQL Injection: Hacker attack')
        break
    print(f'Processing Email: {email}')
#  Else in Loops
#  Run a block of code only if the loop finishes naturally
items = [ 1, 3, 4, 7]
for i in items:
    print(i)
print("Loop is completed")
# Use Else in loops when there is a break 
items = [1,3,5, 7]
for i in items:
    if i % 2 == 0:
        print("Even Nr. found", i)
        break
else:
    print("All numbers are odd")
# Task Check for Missing Names in a List
names = ["Mummy","Neha"," nirali","Harshi"]
for name in names:
    if name is None:
        print("found missing name")
        break
else:
    print("All names are available")

# Task check if all files are csv files
files = ['data1.csv',
         'report.pdf',
         'data2.txt'
         'report,csv'
]
for file in files:
    if not file.endswith('.csv'):
        print(f'Not all files are csv')
        break
else:
    print('All files are CSV')
# else + Continue makes no logic to use
# Python Challenge 
# Check whether any filename appears more than once
# print "Duplicates found" if a duplicate exists,otherwise print "all files are unique"
file_list=[
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'data.txt',
    'report.csv'
]
seen_file = []
has_duplicate = False
for file in file_list:
    if file in seen_file:
        has_duplicate = True
        break
    seen_file.append(file)
if has_duplicate:
    print("Duplicate found")
else:
    print("all files are unique")

# Nested loop
for x in range(3):
    for y in range(2):
        for z in range(2):
            print(f"({x}, {y}, {z})")

# use case of nested loop :- crossing data
colors = ['red', 'blue','green']
sizes = ['L', 'M', 'S']
for color in colors:
    for size in sizes:
        print(f'{color} - Size {size}')
#  use case :- navigate hierarchy
years = [2026, 2027]
months = ['Jan','Feb']
days = range(1,29)

for y in years:
    for m in months:
        for d in days:
            print(f'report_{y}_{m}_{d}.csv')

tables = ['customers','orders','prices']
columns =['id','create_date']
for t in tables:
    for c in columns:
        print(f'SELECT count(*) from {t} WHERE {c} is NULL;')

# While loop
count = 1
while count <= 10:
    print (count)
    count += 2

# answer = ""
# while answer != "yes":
#     answer = input("Do you agree?(yes/no): ")
# print("Thank you ")

#  Belove is infinite loop 
# while True:
#     print('I am unstopable')

# while True:
#     answer = input("Do you agree? (yes/no): ")
#     if answer == "yes":
#         break
# print("Thank you")



# Challenge 
n = 0
while True and n<=3:
    answer = input("Do you agree ? (yes/no):")
    n += 1
    if answer == "yes" and n<=3:
        print("Glad we are on the same page")
        break
    elif n==3 :
        print("3 strik, You are Out!")
        break

print("Thank you")
# Allow up to 3 attempts
#  if the user types "yes",print" Glad we are on same page

attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we are on the same page")
    attempts += 1
else:
    print("3 strikes. you are out!")