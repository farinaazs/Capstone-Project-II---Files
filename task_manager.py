"""
==== Capstone project template ====

- Create a Login Section
    > read usernames and passwords from the user.txt file to validate the user
    > the user to enter their username and password until it matches
    > once validated, open the menu section

- Create 2 different Menu Sections
    >> if the user_name IS "admin" and the pass_word is "adm1n"
        - open following menu:
            r - Registering a user
            a - Adding a task
            va - View all tasks
            vm - view my task
            ds - display statistics
            e - Exit
    >> if the user_name is NOT "admin and the pass_word is NOT "adm1n"
        - open following menu:
            r - Registering a user
            a - Adding a task
            va - View all tasks
            vm - view my task
            e - Exit

- If menu == "r - Registering a user"
    >> if the user is NOT "admin"
        - not authorized to register a new user

    >> if the user IS "admin"
        - register new user
            - loop over the user.txt file to validate that the user_name and pass_word
              does not already exist.
            -  should the user_name and pass_word not be in the user.txt file,
              write and append the input data to the user.txt file on a new line

- If menu == "a - Adding a task"
    >> create lists to append the input data for each section of the task requirements
        - request user input for the following data:
            - Task Name             :
            - Task is assigned to   :
            - Date assigned         :
            - Due date              :
            - Task complete (Yes/No):
            - Task description      :
        - write and append data on a new line to the tasks.txt file

- If menu == "va - View all tasks"
    >> open the tasks.txt file in read-only mode
        - display all the tasks in the following format:

            Task            : Assign initial tasks
            Assigned to     : admin
            Date assigned   : 10 Oct 2019
            Due date        : 25 Oct 2019
            Task Complete   : No
            Task description: Use taskManager.py to assign each team member with appropriate tasks

- If menu == "vm - view my task"
    >> open the tasks.txt file in read-only mode
        - loop over the file to verify if the user_name that is logged in
            - if the logged-in user_name is in the tasks.txt file
                > display all Tasks assigned to that user_name
            - if the logged-in user_name is NOT in the tasks.txt file
                > display "You have no tasks or no additional tasks assigned to you."

- If menu == "ds - display statistics"
    >> open the tasks.txt file in read-only mode
        - read the lines on the tasks.txt file
        - print(f"\nThe total number of Tasks are: {len(file_lines)}")

    >> open the user.txt file in read-only mode
        - read the lines on the user.txt file
        - print(f"The total number of Users are: {len(users_file_lines)}")

- If menu == "e - Exit"
    >> exit the infinite loop

- if the user makes an invalid entry:
    print("You have made a wrong choice, Please Try again")
    the menu will loop back again.
"""

# ============== Importing Libraries ============= #
"""This is the section where you will import libraries"""

# ================= Login Section ================ #
print("\n**** PLEASE LOGIN ***")

# created lists to loop over in the user.txt file
usernames = []
passwords = []

# opening the user.txt file in 'read only' mode
# striping and splitting each list
with open("user.txt", "r") as file:
    for lines in file:
        temp = lines.strip()
        temp = temp.split(", ")

        usernames.append(temp[0])  # appending all the user_names to the usernames list
        passwords.append(temp[1])  # appending all the pass_words to the passwords list

# requesting the user to enter their credentials
user_name = input("\nPlease enter your username: ")
pass_word = input("Please enter your password: ")

# continuously looping over the lists until the conditions become True
while True:
    if user_name in usernames and pass_word in passwords:
        print(f"\nThank you and Welcome, {user_name}!")

    elif user_name and pass_word != usernames and passwords:
        print("\nYour username and/or password is incorrect. Please try again.")
        user_name = input("\nPlease enter your username: ")
        pass_word = input("Please enter your password: ")
        continue
    break
file.close()

# ================= Menu Section ================= #
# creating an infinite loop so that the user comes back to the menu section repeatedly
# after a selection has been executed
while True:  # presenting the menu to the user
    # if the user is NOT "admin" the standard option will be generated
    if user_name != "admin" and pass_word != "adm1n":
        menu = input('''\n*** MENU SECTION ***
        
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()  # making sure that the user input is converted to lower case.
    else:  # if the user IS "admin" the customised option will be generated
        menu = input('''\n*** MENU SECTION ***
        
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
ds - display statistics
e - Exit
: ''').lower()  # making sure that the user input is converted to lower case.

    # =============== Registering a new user =============== #
    # if the logged-in user is not "admin", they are unable to add a new user
    if user_name != "admin" and pass_word != "adm1n" and menu == "r":
        print("\n*** REGISTERING A NEW USER ***")
        print(f"\nUnfortunately {user_name}, you are not authorized to register a new user.")

    # if the logged-in user is "admin", they authorized to add a new user
    elif user_name == "admin" and pass_word == "adm1n" and menu == "r":
        print("\n*** REGISTERING A NEW USER ***")

        # lists to loop over in the user.txt file
        usernames = []
        passwords = []

        with open("user.txt", "r") as file:
            for lines in file:
                temp = lines.strip()
                temp = temp.split(", ")

                usernames.append(temp[0])  # appending the new_user_name to the usernames list
                passwords.append(temp[1])  # appending the new_pass_word to the passwords list

        # requesting the new_user_name input
        new_user_name = input("\nPlease enter the new username         : ")
        while new_user_name in usernames:  # looping over until condition is True
            print("*** This username already exists! ***")
            new_user_name = input("\nPlease enter the new username         : ")

        # requesting the new user's pass_word input
        new_pass_word = input("Please enter the new user password    : ")
        while new_pass_word in passwords:  # looping over until condition is True
            print("*** This password already exists! ***")
            new_pass_word = input("\nPlease enter the new user password    : ")

        # checking that the passwords match
        # if matched, the program adds the new_user_name and new_pass_word to the user.txt file
        confirm_password = input("Please confirm the new user password  : ")
        if new_pass_word == confirm_password:
            print("\nThe passwords match")
            file = open("user.txt", "a")
            file.write(f"\n{new_user_name}, {new_pass_word}")
            file.close()
            print("\nThank you! The new user credentials have been added to the 'user.txt' file.")
        else:
            print("\n*** The passwords do not match! ***")
            new_pass_word = input("\nPlease reconfirm the new user password: ")
            file = open("user.txt", "a")
            file.write(f"\n{new_user_name}, {new_pass_word}")
            file.close()
            print(f"\nThank you! The new user credentials have been added to the 'user.txt' file.")

    # =============== Adding a new Task =============== #
    elif menu == 'a':
        print("\n*** ADD A NEW TASK ***")
        # created lists to append the input data when adding a new task
        task = []
        assigned_to = []
        date_assigned = []
        due_date = []
        task_complete = []
        task_description = []

        with open("tasks.txt", "r") as task_f:
            for lines in task_f:
                temp = lines.strip()
                temp = temp.split(", ")

                task.append(temp[1])  # task name
                assigned_to.append(temp[0])  # assigned to user
                date_assigned.append(temp[3])  # assigned date
                due_date.append(temp[4])  # due date
                task_complete.append(temp[5])  # Yes/No
                task_description.append(temp[2])  # Description of the task

        _task = input("\nTask Name             : ").capitalize()
        _assign_to = input("Task is assigned to   : ")
        _date_assign = input("Date assigned         : ").capitalize()
        _due_date = input("Due date              : ").capitalize()
        _task_complete = input("Task complete (Yes/No): ").capitalize()
        _task_desc = input("Task description      : ").capitalize()

        # opening the tasks.txt file in 'append' mode
        # writing the input data to the tasks.txt file on a new line
        task_f = open("tasks.txt", "a")
        task_f.write(f"\n{_assign_to}, {_task}, {_task_desc}, {_date_assign}, {_due_date}, {_task_complete}")
        task_f.close()
        print("\nThank you! The new Task has been added to the 'task.txt' file.")

    # =============== Viewing All Tasks =============== #
    elif menu == 'va':
        print("\n*** VIEWING ALL TASKS ***")
        # displays all the Tasks in the tasks.txt file
        # open tasks.txt file in read-only mode
        with open("tasks.txt", "r") as task_f:
            for lines in task_f:
                temp = lines.strip()
                temp = temp.split(", ")
                # the text will display as Output 2 in the Capstone pdf
                print(f"""
Task            : {temp[1]}
Assigned to     : {temp[0]}
Date assigned   : {temp[3]}
Due date        : {temp[4]}
Task Complete   : {temp[5]}
Task description: {temp[2]}""")
        task_f.close()
        print(f"\nThank you, {user_name}! These are all the current Tasks in the 'tasks.txt file.")

    # =============== Viewing My Tasks =============== #
    elif user_name == temp[0] and menu == 'vm':
        print("\n*** VIEWING MY TASKS ***")
        # display all the tasks assigned to the user that is currently logged in
        with open("tasks.txt", "r") as task_f:
            for lines in task_f:
                temp = lines.strip()
                temp = temp.split(", ")
                while user_name == temp[0]:
                    # the text will display as Output 2 in the Capstone pdf
                    print(f"""
Task            : {temp[1]}
Assigned to     : {temp[0]}
Date assigned   : {temp[3]}
Due date        : {temp[4]}
Task Complete   : {temp[5]}
Task description: {temp[2]}
""")
                    break
                # if the user has no tasks or no additional tasks assigned to them
                if user_name != temp[0]:
                    print("\nYou have no tasks or any additional tasks assigned to you.")
                    break

        task_f.close()
    # =============== Display Statistics ============== #
    elif menu == 'ds':
        print("\n*** DISPLAYING STATISTICS ***")

        # displays the total number of tasks in the tasks.txt file
        file = open("tasks.txt", "r")
        file_lines = file.readlines()
        print(f"\nThe total number of Tasks are: {len(file_lines)}")
        file.close()

        # displays the total number of users listed in the user.txt file
        users_file = open("user.txt", "r")
        users_file_lines = users_file.readlines()
        print(f"The total number of Users are: {len(users_file_lines)}")
        users_file.close()

    # =============== Exiting the Menu =============== #
    elif menu == 'e':
        # exiting the menu and ending the program
        print(f"\nGoodbye and see you soon, {user_name}!!!")
        exit()

    # ============== Invalid Selection =============== #
    else:
        print("You have made a wrong choice, Please Try again")

# Thank you, Farinaaz :)
