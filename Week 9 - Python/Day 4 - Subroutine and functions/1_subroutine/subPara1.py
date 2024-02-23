"Parameter(s): used in a subroutine/function to allow values to be passed into them/used as a placeholder(s)"

"To Do: Predict, then Run, and then Investigate"

# define the subroutine/function addition with parameters par1 and para2
"In the subroutine definition, you pass in the parameter(s)(placeholder(s))"
def addition(num1, num2):
    answer = num1 + num2
    #print(f"The answer to {num1} + {num2} = {answer}")
    return answer

"in the subrotuine call, you pass in the argument(s)"
answer = addition(int(input("Enter first number:")), int(input("Enter second number:")))
print(answer)

"Make/Modify"
"To Do: Task 1 : Modify the subroutine call below to pass in you own name as an argument "
usernum1 = int(input("Enter first number:"))
usernum2 = int(input("Enter second number:"))

addition(usernum1, usernum2)


#if __name__ == "__main__":
    # Method 1
    # in the subroutine call we pass in the integer values(1,2) within the braces as an argument to be passed
    # into the parameters par1 and para2
  
   

   

    # Method 2
    # in the subrotuine call we pass in the variable name  within the braces as an argument to be passed
    # into the parameter paraUname
    #in the subroutine call we pass in the num1 and num2  within the braces as an argument to be passed
    #into the parameters par1 and para2
  
   

