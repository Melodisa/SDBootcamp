fname    = input("Enter you full name: ")
address   = input("Enter your address: ")
interest = input("Enter your interest: ")
age      =    int(input("Enter your age: "))

# create a dictionairy 
userData = {
     "Fullname": fname, 
     "Address": address,
     "interest": interest,
     "age": age}

"Make"
"To Do: Task 1: Use the code above to ask for user input and then save it to a file called userDetails.txt"
with open('Week 10 - Pyton\Day 6\Week 10 Codebase\Pt7_FilesDictsCodeBase2024\2_Records_Collections\2_userDetails.txt', 'a') as addData:
    for aKey, aValue in userData.Items(): 
        addData.write(f"key: {aKey}, Value: {aValue}")
    # addData.write("\n" +fname+ "\n" +address+ "\n" +interest+ "\n" str(+age+)) #the age will be written as string value




"Further reading"
# https://www.w3schools.com/python/python_file_handling.asp