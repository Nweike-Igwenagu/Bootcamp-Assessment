# Chinweike Igwenagu
# +2349135304466

# here we imported re so we can use regular expression later in the code
import re

# now we ask the user to input his/her name
name = input("Whats your name? ")

# here we are validating to make sure that the name is a string whose length is in the range of 2-64
while not (name.isalpha() and 2<=len(name)<=64):
    print("invalid input!")
    name = input("Whats your name? ")

# now if thats sucessful we would procced to ask for their age
age = input("Enter your Age ")

# here we re validating and making sure the age is a digit in the range of 16-30
while not (age.isdigit() and 16<=int(age)<=30):
    print("invalid input!")
    age = input("Enter your Age ")
    
# now if thats sucessful we would procced to ask for their department
department = input("whats your Depertment? ")

# here we are validating and making sure the department is a sequence of characters
while not (department.isalpha()):
    print("invalid input!")
    department = input("whats your Depertment? ")

# now if thats sucessful we would procced to ask for their registration number
reg_no = input("Enter your registration number ")

# here we use regular expression to validate the reg_no for the format xxxx/yyyyyy
while not re.match(r"^(19[9-9][0-9]|20[0-2][0-4])/\d{6}$", reg_no):
    print("Invalid input!")
    reg_no = input("Enter your registration number ")

# here we create an empyt list details
details = []

# here name,age,department and reg_no was appended to the empty list
details.append(name)
details.append(age)
details.append(department)
details.append(reg_no)

# now we re finally using list indexing to display the users name as a message
print(f"Your name is {details[0]}")