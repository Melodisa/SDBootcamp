# Selection is used to control the flow of the program

# elif == else if

score = int(input("Enter a number: "))
"Predict, then Run, and then Investigate"
# check the condition that score is greater than 100
if score > 100:
# create a variable and assign it the value Invalid Entry
    grade = "Invalid Entry"
# check the condition that score is between 75 and 100
elif score <=100 and score >=75:
# create a variable and assign it the value A
    grade = "A"
# check the condition that score is between 60 and 74
elif score <=74 and score >=60:
# reassign the grade variable the value B
    grade = "B"
# check the condition that score is between 50 and 59
elif score <=59 and score >=50:
# reassign the grade variable the value C
    grade = "C"
# reassign the grade variable the value F
else:
    grade = "F"

print(grade)

#ToDo: Q&A
"What do you think is the equivalent of JS else if in python?"


"Make"
#ToDo: Task 1: Using if elif and else
# Create a Menu program that allows users to select between three subject choices
# User must be presented with the value assoiciated with each choice
# for example 1. Music, 2. Maths ....
# A choice must also be available for the user to exit the program
# A message using the print function must be display as per the user choice


subject1="art"
subject2="Fashion"
subject3="Math"
print("options of subjects: {subject1}, {subject2}, {subject3}")
subjects=int(input("enter your subject:"))
if subjects == subject1:
message=f"you have selected art, nice!"
elif subjects == subject2:
message=f"You have chosen fashion, great!"
elif subjects == subject3:
message=f"you have picked math, alright genius!"
else: 
message="error! Please select a subject or exit page!"
print(message)




#ToDo: Task 2
# Use if else to find item(a specific number) from a list
numList = [56, 78, 100, 45, 88, 71]

# the list
numList = [56, 78, 100, 45, 88, 71]

#  numbers to find
target_number = 56
target_number = 78
target_number = 100
target_number = 45
target_number = 88
target_number = 71

# checking if the target number is in the list
if target_number in numList:
    print(f"{target_number} is found in the list")
else:
    print(f"{target_number} is not found in the list")
