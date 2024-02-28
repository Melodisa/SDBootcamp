num1 = int(input(("Enter your first number: ")))
num2 = int(input(("Enter your second number: ")))
answer = num1 / num2

print(answer)
print("Execute the following code...\n....\n......\n...\n...")


try: #try or run the code within the try block


try: # test run or try the code within the try block
    num1 = int(input("Enter your first number: "))
    answer = num1
    print(answer)
    

except ZeroDivisionError: # handle or deal with ZeroDivisionError
    print("You can't divide a whole number by Zero")
print("Execute the following code...\n....\n......\n...\n...")

finally:
print("Operation completed")

print("Execute the following code...\n")