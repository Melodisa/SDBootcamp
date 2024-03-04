import readsongs, addsongs, updatesongs, deletesongs, reports

def read_file(file_path): #file_path is a parameter/variable
    try:
        #with open('Week 10 Codebase/ Pt7_FilesDictsCodeBase2024/file3.txt',"a") as filePath1:
        with open(file_path) as readFile:
            rf = readFile.read()
            return rf
    except FileNotFoundError as nf:
        print(f"file not found because: {nf}")
# test to retrive or load menuOptions.txt file 
        
print(read_file("Week 10 Codebase/Pt9_10DB/menuOptions.txt"))
    
def songs_menu():
    option = 0 # initialise/assign the option variable  wint an integer value 0
    # create a list of string values/elements/items
    optionsList = ["1","2","3","4","5","6"]
    # call the read file function and assign it to a variable call menuChoices
    menuChoices = read_file("Week 10 Codebase/Pt9_10DB/menuOptions.txt")
    read_file()
    file_path = "Week 10 Codebase/Pt9_10DB/menuOptions.txt"

    #repeat the menu options until the option to exit the menu is entered
    while option not in optionsList:
        #print the menuoptions repeatedly by calling the variable 
        #that hold the read_file function in the print statement
        print(menuChoices)

        # re-assign the value of the option variable so it can be re-used
        option = input("Enter an option from the menu choices above:  ") # 1 = "1" or 2 = "2"
        
        # check if the input value entered in the option variable above is not outside of 1,2,3,4,5,6
        if option not in optionsList:
            print(f"{option} is not a valid choice!!! ")
    return option

mainProgram = True #Toggle to False to exit the while loop below
while mainProgram: #same as while True
    # call the songs_menu() function and assign it to a variable
    mainMenu = songs_menu()

    # 
    if mainMenu == "1":
        # call the readsong file imported on line one and the function inside of it called  read_songs()
        readsongs.read_songs()
    elif mainMenu == "2":
        addsongs.insert_songs()
    elif mainMenu == "3":
        updatesongs.update_song()
    elif mainMenu == "4":
        deletesongs.delete_song()
    elif mainMenu == "5":
        reports.search_song()
    else:
        mainProgram = False # set the mainProgram vaiable to False exit the menu
input("Press enter to exit the...")


    















