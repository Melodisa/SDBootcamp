"Read data structures and record for 2 minutes"
"""
Data structures are used to store data in an organised and accessible way. 
A list is a data structure.  Another example of a data structure is a record.  
You might have heard of the word record if you have ever created a database before. 


A record allows you to store a collection of attributes for a single entity.
Data structure: record: An entity can be any object, place, person, or thing. 
Attributes are properties or characteristics of that entity.  
Attributes are sometimes referred to as fields. 

"""


"To Do: Predict, then Run, and then Investigate"
# create a dictionary
# dictionaryVariable = {"key":"value","key":"value", "key":"value","key":"value","key":"value"}
dict1 = {"fName":"Em Jay", "interest":"Coding", "age":23, "Gamer":True}
print(dict1)
print(dict1["fName"])
print(dict1["Gamer"])
 
mylist = ["A","B","C"]
print(mylist[1])
 
 
"Using dictionary methods"
print("\nUsing dictionary methods")
# D.items() -> a set-like object providing a view on D's items
dItems = dict1.items()
# print(dict1.items())
print(dItems)
 
# D.keys() -> a set-like object providing a view on D's keys
dKeys = dict1.keys()
print(dKeys)
 
# D.values() -> an object providing a view on D's values
dVals = dict1.values()
print(dVals)
print("\n")
"""To Do: Task 1: Refer to the example code above to create your
own dictionary with key value pairs and explain the differences between the items(), keys() and values() dictionary methods"""
 
cardict = {
  "brand": "Ford",
  "model": "Corvette",
  "year": 1988
}
print(cardict)


# Loop through the keys and/values
print("\nLoop through the keys and/values")
for key, value in dict1.items(): #dItems:
    print(f"Key: {key}, Value: {value} ")
 
print("\nLoop through the keys ")
for key in dKeys:
    print(f"Key: {key}")
 
print("\nLoop through the values")
for value in dVals:
    print(f"Value: {value} ")
 
 
print("\n")
"To Do: Task 2: Modify"
# Modify: The for loop block above to loop through your own the values
 
"To Do: Extension: Can you use the for loop with the items method to loop through the keys and values simultaneously"
# Modify: The for loop block above to loop through the keys and the values and format your output
 
# create a dictionary
dict2 = {2:"Python", 3:"HTML", 4:"CSS"}
print(f"Dictionary 2 {dict2}")
 
 
# Use of the Update method to merge two dictionaries
 
dict1.update(dict2)
print(f"Updated dictionary 1\n{dict1}")
 
 "To Do: Task 2: Research: Look up Pop vs popItem explaind comment the code below to explain the difference"
 

"Pop method removes a key from a dictionary and returns its value"
"popitem "
# # Add comment here to explain the function of th pop() method.
dict2.pop(3) #removes a specific value
print(dict2)
 
# # Add comment here to explain the function of th popItem() method.
dict1.popitem() #removes only the last value
print(dict1)
 
 
# "Delete key-value pair from dictionary:"
# # We can delete a key-value pair from a dictionary using the del keyword followed
# # by the key value to be deleted enclosed in [].
 
del dict1[2]
 
 
# # update dictionary value using the key
dict1[1] = "Emma Smith"
 
user={"interests" :"coding"}
print(user)
 
user["interests"] = "Football"
 
print(dict1)
print(user)