import addFilms, readfilms, updatefilms,reports, deleteFilms

def read_file(file_path): #file_path is a parameter/variable
    try:
        with open(file_path) as readFile:
            rf = readFile.read()
            return rf
    except FileNotFoundError as nf:
        print(f"file not found because: {nf}")
        
def film_menu():
    option = 0 # initialise/assign the option variable  wint an integer value 0
    # create a list of string values/elements/items
    optionsList = ["1","2","3","4","5"]
    # call the read file function and assign it to a variable call menuChoices
    menuChoices = read_file("Week 11 - Pyhon Project/Textfiles/Filmmenu.txt")

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

def report_menu():
    option = 0 
    optionsList = ["1","2","3","4","5"]
    menuChoices = read_file("Week 11 - Pyhon Project/Textfiles/Reportmenu.txt")

    while option not in optionsList:
        print(menuChoices)
        option = input("Enter an option from the menu choices above:  ") 
        if option not in optionsList:
            print(f"{option} is not a valid choice!!! ")
    return option

def menu_select():
    option = 0 
    optionsList = ["1","2","3"]
    menuChoices = read_file("Week 11 - Pyhon Project/Textfiles/Menuselect.txt")

    while option not in optionsList:
        print(menuChoices)
        option = input("Enter an option from the menu choices above:  ") 
        if option not in optionsList:
            print(f"{option} is not a valid choice!!! ")
    return option

mainProgram = True
while mainProgram == True: 
    mainMenuChoice = menu_select()

    if mainMenuChoice == "1": 
        while True:
            film_choice = film_menu()
            if film_choice == "1":
                addFilms.insert_films()
                pass
            elif film_choice == "2": 
                deleteFilms.delete_song()
                pass
            elif film_choice == "3":
                updatefilms.update_tblFilms()
                pass
            elif film_choice == "4":
                readfilms.read_films()
            elif film_choice == "5":
                break
            
    elif mainMenuChoice == "2":
        while True:
            report_choice = report_menu()
            if report_choice == "1":
                addFilms.insert_films()
                pass
            elif report_choice == "2": 
                deleteFilms.delete_song()
                pass
            elif report_choice == "3":
                updatefilms.update_tblFilms()
                pass
            elif report_choice == "4":
                readfilms.read_films()
            elif report_choice == "5":
                break














