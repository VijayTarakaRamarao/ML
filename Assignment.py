print("\n")
print("Question 1")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print("Sorted Ages List:", ages)
# "min" Gives the minimum number from list
min_age = min(ages)
# "max" Gives the maximum number from list
max_age = max(ages)
print("Minimum Age:", min_age)
print("Maximum Age:", max_age)

# Add the min age and the max age again to the list
# "append" adds the element to the list
ages.append(min_age)
ages.append(max_age)
print("Updated List of Ages with Min and Max Ages:", ages)

ages.sort()
# Find the median age (one middle item or two middle items divided by two)
# Get the length of the list and Divide the length by 2
# if reminder is 0, Then get the middle and middle -1 element and divide by 2
# if reminder is other than 0, Then get the middle element and divide by 2
lst_Length = len(ages)
print("Ages List Length:", lst_Length)
num = lst_Length // 2
if lst_Length % 2 == 0:
    middlenumber = (ages[num] + ages[num - 1]) / 2
else:
    middlenumber = ages[num]/2
print("Median Age Value:", middlenumber)

# Find the average age (sum of all items divided by their number)
# Iterate the element in ages and add it total counter-"sum-num" and then divide by the length of the list
sum_num = 0
for t in ages:
    sum_num = sum_num + t
avg_ages = sum_num / len(ages)
print("Average Age:", avg_ages)

# Find the range of the ages (max minus min)
print("Range of Ages:", max_age - min_age)

# Question 2
print("\n")
print("Question 2")
# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Jimmy'
dog['color'] = 'Black'
dog['breed'] = 'Doberman'
dog['legs'] = 4
dog['age'] = 7
print("Dog Dictionary:", dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country,
# city and address as keys for the dictionary
student = {'first_name': 'Steve', 'last_name': 'Rogers', 'gender': 'Male', 'age': 25, 'marital status': 'Unmarried',
           'skills': ['Python', 'Java'], 'country': 'USA', 'city': 'Newyork', 'address': 'Saint Street'}
print("Student Dictionary:", student)

# Get the length of the student dictionary
print("Length of Student Dictionary:", len(student))

# Get the value of skills and check the data type, it should be a list
student_skills = student.get('skills')
print("Existing Student skills:", student_skills)
print("Data type of Student skills:", type(student_skills))

# Modify the skills values by adding one or two skills
student.update({'skills': ['React, JavaScript']})
print("Update Student skills:", student.get('skills'))

# Get the dictionary keys as a list
print("Student Dictionary Keys:", student.keys())

# Get the dictionary values as a list
print("Student Dictionary Value:", student.values())

# Question 3
print("\n")
print("Question 3")

# Create a tuple containing names of your sisters and your brothers
brother = ('Steve', 'Jim')
sisters = ('Rachel', 'Jessy')

# Join brothers and sisters tuples and assign it to siblings
siblings = brother + sisters
print("The total siblings data is:", siblings)

# How many siblings do you have?
print("Total No of siblings:", len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father_name = ('John',)
mother_name = ('Jenny',)
family_members = siblings + father_name + mother_name
print("Family Members Info:", family_members)

# Question 4
print("\n")
print("Question 4")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print("Length of set of IT Companies", len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Verizon", "Dell"])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("Twitter")
print(it_companies)

# What is the difference between remove and discard

# Both the Remove and discard methods are used to remove the specified item from the set
# by passing as argument to respective methods. The difference between those two are
# "Remove" method raises a KeyError exception
# "Discard" method does not raise an exception

# Join A and B
print("Union of A & B sets:", A | B)

# Find A intersection B
print("Intersection of A & B sets:", A & B)

# Is A subset of B
print("Is A subset of B:", A <= B)

# Are A and B disjoint sets
print("Are A and B disjoint sets:", A.isdisjoint(B))

# Join A with B and B with A
print("Join A with B:", A.union(B))
print("Join B with A:", B.union(A))

# What is the symmetric difference between A and B
print("symmetric difference:", A.symmetric_difference(B))

# Delete the sets completely
print("After Clearing set A, Elements in A:", A.clear())
print("After Clearing set B, Elements in B:", B.clear())

# Convert the ages to a set and compare the length of the list and the set.
age_set = {x for x in age}
print("Convert the ages to a set:", age_set)
print("Length of Ages List", len(age))
print("Length of Ages Set", len(age_set))

# Question 5
print("\n")
print("Question 5")

# Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
radius_of_circle = 30
PI = 3.142
_area_of_circle_ = PI * (radius_of_circle * radius_of_circle)
print("Area of Circle", _area_of_circle_)

# Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
_circum_of_circle_ = 2 * PI * radius_of_circle
print("Circumference of Circle", _circum_of_circle_)

# Take radius as user input and calculate the area
radius_input = float(input(' Please Enter the radius of a circle: '))
_input_area_of_circle_ = PI * (radius_input * radius_input)
print("Area of Circle with user Input radius:", _input_area_of_circle_)

# Question 6
print("\n")
print("Question 6")
# “I am a teacher and I love to inspire and teach people”
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
str1 = "I am a teacher and I love to inspire and teach people"
set_of_String = str1.split()
unique_elements = set(set_of_String)
print(unique_elements)

# Question 7
print("\n")
print("Question 7")
# Use a tab escape sequence to get the following lines.
# Name Age Country City
# Asabeneh 250 Finland Helsinki
print("Name \tAge \tCountry \tCity")
print("Asabeneh \t250 \tFinland \tHelsinki")

# Question 8
print("\n")
print("Question 8")
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# “The area of a circle with radius 10 is 314 meters square.”
radius = 15
area = 3.14 * radius ** 2
print("The area of a circle with radius %d is %d meters square." % (radius, area))

# Question 9
print("\n")
print("Question 9")
# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a
# separate list using Loop. N: No of students (Read input from user)
lbs_list = []
kgs_list = []
no_of_students = int(input("Enter the list size "))
print("\n")
for i in range(0, no_of_students):
    print("Enter number at index", i, )
    lbs_input = int(input())
    lbs_list.append(lbs_input)
    kgs_wgt = round((lbs_input / 2.2046), 2)
    kgs_list.append(kgs_wgt)
print("Pounds List:", lbs_list)
print("Kilograms List:", kgs_list)










