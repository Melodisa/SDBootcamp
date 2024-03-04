import FirstTryDB.readfilms as readfilms, FirstTryDB.addFilms as addFilms, updatefilms, FirstTryDB.deleteFilms as deleteFilms, reports

def read_file(file_path): #file_path is a parameter/variable
    try:
        with open('Week 10 - Pyton\Day 6\Week 10 Codebase\Pt7_FilesDictsCodeBase2024/file3.txt',"a") as filePath1:
        with open(file_path) as readFile:
            rf = readFile.read()
            return rf
    except FileNotFoundError as nf:
        print(f"file not found because: {nf}")
# test to retrive or load menuOptions.txt file 
        
# print(read_file("Week 10 Codebase/Pt9_10DB/menuOptions.txt"))
        
def Title_menu():
    option = 0 # initialise/assign the option variable  wint an integer value 0
    # create a list of string values/elements/items
    optionsList = ["1","2","3","4","5","6"]
    # call the read file function and assign it to a variable call menuChoices
    menuChoices = read_file("FirstTryDB/menuOptions.txt")

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
    mainMenu = Title_menu_menu()

    # match case is the euivalent of switch stament in JavaScript
    match mainMenu:
        case "1": # call the readsong file imported on line one and the function inside of it called  read_songs()
            readfilms.read_songs()
        case "2":
                addFilms.insert_songs()
        case "3":
            updatesongs.update_song()
        case "4":
            deleteFilms.delete_song()
        case "5":
            reports.search_song()
        case _:
            mainProgram = False # set the mainProgram vaiable to False exit the menu
input("Press enter to exit the...")


    















