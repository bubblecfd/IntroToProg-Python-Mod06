# ------------------------------------------------------------------------ #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoFile.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# RRoot,1.1.2030,Fixed bug by clearing the list before it was refilled
# Tao Ye, 5.19.2020, Modified code to complete assignment 6
# Tao Ye, 5.20.2020, Revision to correct FileProcessor.FindFile method
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """ Processing the data to and from a text file """

    @staticmethod
    def ReadFileDataToList(file_name, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows
        """
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"Task": data[0].strip(), "Priority": data[1].strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def WriteListDataToFile(file_name, list_of_rows):
        """
        Desc - Save a list of dictionary rows to a file

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want to save to the file
        :return: (string) message to the user about the file save
        """
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
        file.close()

    @staticmethod
    def FindFile(file_name):
        """
        Desc - Locate a file for subsequent file read

        :param file_name: (string) with name of file
        :return: (Boolean) True: file exists; False: file not found
        """
        try:
            file = open(file_name)
            file.close()
            return True
        except FileNotFoundError:
            return False

class ListOperations:
    """ Operations to manipulate the list of dictionary rows """

    @staticmethod
    def AddNewItemToList(list_of_rows, task, priority):
        """ Add a new item to the list

        :param list_of_rows: (list) of rows to which a new item is added
        :param task: (string) new task name
        :param priority: (string) new task priority
        :return: list is passed by reference, and will be updated
        """

        taskExist = False

        for row in list_of_rows:
            if (row["Task"].lower() == task.lower()):
                taskExist = True
                break

        if (not taskExist):
            row = {"Task": task, "Priority": priority}  # Create a new dictionary row
            list_of_rows.append(row)  # Add the new row to the list/table
        else:
            print("I am sorry, duplicate task in the list")

        print()

    @staticmethod
    def RemoveItemFromList(list_of_rows, taskToRemove):
        """ Remove an item from the list

        :param list_of_rows: (list) of rows from which a task is removed
        :param taskToRemove: (string) task to be removed
        :return: list is passed by reference, and will be updated
        """

        taskExist = False

        # Search though the table or rows for a match to the user's input
        for row in list_of_rows:
            if (row["Task"].lower() == taskToRemove.lower()):
                list_of_rows.remove(row)
                taskExist = True

        # Update user on the status of the search
        if (taskExist):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")

        print()  # Add an extra line for looks
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ A class for perform Input and Output """

    @staticmethod
    def OutputMenuItems():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Reload Data from File
        6) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        """ Shows the current items in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current items ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def InputTaskAndPriority():
        """ Ask the user to enter task and priority

        :param none:
        :return: (string) task and priority
        """
        task = str(input("What is the task? - ")).strip()
        priority = str(input("What is the priority? [high|low] - ")).strip()
        return task, priority
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
# If the file already exists, load data from the file
if FileProcessor.FindFile(strFileName):
    FileProcessor.ReadFileDataToList(strFileName, lstTable)  # read file data
else:
    print("File", strFileName, "does not exist yet.")

# Step 2 - Display a menu of choices to the user
while(True):
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    # Step 3 - Process user's menu choice
    # Step 3.1 Show current data
    if (strChoice.strip() == '1'):
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.2 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):

        # Ask user for new task and priority
        strTask, strPriority = IO.InputTaskAndPriority()
        print()  # Add an extra line for looks

        # Add item to the List/Table
        ListOperations.AddNewItemToList(lstTable, strTask, strPriority)

        # Show current data in the list/table
        IO.ShowCurrentItemsInList(lstTable)
        continue  # to show the menu

    # Step 3.3 - Remove an item from the list/Table
    elif(strChoice == '3'):

        # Ask user for item to be removed
        strKeyToRemove = input("Which TASK would you like removed? - ")

        # Remove the item from the list
        ListOperations.RemoveItemFromList(lstTable, strKeyToRemove)

        # Show the current items in the table
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.4 - Save tasks to the ToDoFile.txt file
    elif(strChoice == '4'):

        # Show the current items in the table
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table

        # Ask user if they want to save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            FileProcessor.WriteListDataToFile(strFileName, lstTable)
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu

    # Step 3.5 - Reload data from the ToDoFile.txt file (clears the current data from the list/table)
    elif (strChoice == '5'):
        print("Warning: This will replace all unsaved changes. Data loss may occur!")  # Warn user of data loss
        strYesOrNo = input("Reload file data without saving? [y/n] - ")  # Double-check with user
        if (strYesOrNo.lower() == 'y'):
            lstTable.clear()  # Added to fix bug 1.1.2030
            FileProcessor.ReadFileDataToList(strFileName, lstTable)  # Replace the current list data with file data
            IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        else:
            input("File data was NOT reloaded! Press the [Enter] key to return to menu.")
            IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.6 - Exit the program
    elif (strChoice == '6'):
        break   # and Exit

# Main Body of Script  ---------------------------------------------------- #