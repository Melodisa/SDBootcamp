# Selection is used to control the flow of the program

pStudy = input("Enter your program of study: ").title()
curProgram = "Bootcamp"

"Predict, then Run, and then Investigate"

# check the condition that pStudy value is same as the value held in curProgram

# do something/execute the line of code if the condition is checked above true/met - welcome

# The block(else) of code will be executed if the codition in the if block is not true/not met


"Modify"
#ToDo: Exercise
# Modify the code above to use the "!=" operator, or the "not" operator


"Your Turn to: Apply and Build"

"Task 1: Using if and else"
# 1. Create a program that finds the minimum value between two numbers using if else

# Function to find the minimum between two numbers
def find_minimum(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the function and displaying the result
minimum_value = find_minimum(num1, num2)
print(f"The minimum value between {num1} and {num2} is: {minimum_value}")

"Task 2"
# 2.Create a python program to check user's password and print "Logged In" if successful
# else "Not Logged In“ when unsuccessful.

# Function to check user's password
def check_password(user_password, entered_password):
    return user_password == entered_password

# User's password (you can replace this with your own password)
user_password = "securepassword"

# Taking input from the user for entered password
entered_password = input("Enter your password: ")

# Checking the entered password
if check_password(user_password, entered_password):
    print("Logged In")
else:
    print("Not Logged In")


