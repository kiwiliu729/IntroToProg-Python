# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <YOUR NAME HERE>,<DATE>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
file = open(objFile, "r") #read the objFile which is set as "ToDoList.txt"
for row in file: #process each row of the file
    lstRow = row.rstrip("\n").split(",") #rstrip removes the new line character, split(",") splits each row by , and returns a list
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1]} #builds a dictionary for each row (Task:first element and Priority:second element)
    lstTable.append(dicRow) #a list of dictionaries
file.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print(("\n--- items in the list 'Table'"))
        print(lstTable) #print current lstTable list
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        new_input = input("Please type your row of data(please use a comma between the task and priority): ")
        item = new_input.split(",") #split the newly added row of data by comma
        lstTable.append({'Task': item[0], 'Priority': item[1]}) #add the data into current lstTable list
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        remove_row = int(input("Which row of data in the table do you want to remove(please type in numbers): "))
        lstTable.pop(remove_row - 1) #removes the entire row of data from current lstTable list
        print("The chosen row of data has been removed.")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        output_file = "ToDoToDoList.txt" #declare the output file
        output = open(output_file, "w") #open/create the file
        for dictionary in lstTable: #process each dictionary in lstTable list
            output.write('Task' + ': ' + dictionary['Task'] + ', ' + 'Priority' + ': ' + dictionary['Priority'] + '\n') #write file data in the dictionary format
        output.close() #close the file
        print("Data has been saved into file.")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("See you next time:)") #print a finish line
        break  # and Exit the program
