# Chinweike Igwenagu
# +2349135304466

# here is the student class with the attributes name, age and department
class Student:
    def __init__(self, name, age,department ):
        self.name = name
        self.age = age
        self.department = department

# here is the function that requests for each of the three attributes via input and returns them
    def get_details():
        name = input("Whats your name? ")
        age = input("Enter your Age ")
        department = input("whats your Depertment? ")
        
        return name, age, department
    
# here re the three new objects of the student class
# student1 = Student("Harvey", 42, "Law")
# student2 = Student("Mike", 30, "Law")
# student3 = Student("Donna", 35, "Public relations")

# This is an empty list stores the general details obtained frm the user
student_details = []

# This is a counter program that makes the loop run three times to get three different data frm the user
i = 0

while i < 3:
    detail = Student.get_details()
    # this appends the details gotten frm the user to the empty list student_details
    student_details.append(detail)
    i += 1

# this is an empty list that would store the ages provided by the user
age_list = []

# using list indexing, the ages of each student is appended to the list
age_list.append(student_details[0][1])
age_list.append(student_details[1][1])
age_list.append(student_details[2][1])

print (age_list)

# this compares the first two ages in the list to know which is greater
# it keeps record of the name that belongs to the graeatest age while running
if int(age_list[0])>int(age_list[1]):
    older = int(age_list[0])
    name = student_details[0][0]
else:
    older = int(age_list[1])
    name = student_details[1][0]
    
#  the greater from the first two is then compared with the last to determine the greatest
# it also keeps record of the name that belongs to the graeatest age while running
if older<int(age_list[2]):
    older = int(age_list[2])
    name = student_details[2][0]

# finally we print out the name and age of the oldest 
print(f"{name} is the oldest student and they are {older} years old")
