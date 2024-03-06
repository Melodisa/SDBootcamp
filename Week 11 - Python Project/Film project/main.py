import addFilms, readFilms, updateFilms, deleteFilms, reports

def read_file(file_path): #file_path serves as a parameter or variable
    try:
        with open(file_path) as readFile:
            rf = readFile.read()
            return rf
    except FileNotFoundError as nf:
        print(f'File not found because: {nf}')

def films_menu():
    option = 0 # Set the option variable to the integer value of 0
    optionsList = ['1', '2', '3', '4', '5']
    # Invoke the read file function and store the result in a variable named menuChoices.
    menuChoices = read_file("Week 11 - Python Project/Textfiles/Filmmenu.txt")
    
    # Continuously iterate through the menu options until the exit command is inputted.
    while option not in optionsList:
        #print the menuOptions.txt file by calling the variable that holds the read_file function in the print statment
        print(menuChoices)
        
        #re-assign the value of the option variable so it can be re-used
        option = input("Enter an option from the menu choices above: ")
        
        #check if the input entered in the option variable above is not oustide 1,2,3,4,5,6
        if option not in optionsList:
            print(f'{option} is not a valid choice!!!')
    return option

def report_menu():
    option = 0 
    optionsList = ['1', '2', '3', '4', '5']
    menuChoices = read_file("Week 11 - Python Project/Textfiles/Reportmenu.txt")

    while option not in optionsList:
        print(menuChoices)
        
        option = input("Enter an option from the menu choices above: ")
        
        if option not in optionsList:
            print(f'{option} is not a valid choice!!!')
    return option

def main_menu():
    option = 0 
    optionsList = ['1', '2', '3']
    menuChoices = read_file("Week 11 - Python Project/Textfiles/Menuselect.txt")
    
    while option not in optionsList:
        print(menuChoices)

        option = input("Enter an option from the menu choices above: ")
        
        if option not in optionsList:
            print(f'{option} is not a valid choice!!!')
    return option

mainProgram = True
while mainProgram:
    mainMenuChoice = main_menu()
    
    if mainMenuChoice == "1":
        while True:
            films_choice = films_menu()
            if films_choice == "1":
                addFilms.insert_films()
                pass
            elif films_choice == "2":
                deleteFilms.delete_film()
                pass
            elif films_choice == "3":
                updateFilms.update_film()
                pass
            elif films_choice == "4":
                readFilms.read_films()
                pass
            elif films_choice == "5":
                break
    elif mainMenuChoice == "2":
        while True:
            report_choice = report_menu()
            if report_choice == "1":
                reports.showAll()
                pass
            elif report_choice == "2":
                reports.searchByGenre()
                pass
            elif report_choice == "3":
                reports.searchByYear()
                pass
            elif report_choice == "4":
                reports.searchByRating()
                pass
            elif report_choice == "5":
                break
    elif mainMenuChoice == '3':
        break
    else:
        print("Invalid choice!")
        
    if input("Do you want to continue? (yes/no): ").lower() != "yes":
        mainProgram = False

print("Exiting....")















