#Task 25
#Compulsory Task 1
#Meshailen Chetty
#27/03/2020

#defined my functions before everything

#created a register function
def reg_user():

    #opened a textfile 
    textfile = open("user.txt","r")
    #asked the user to input their name they are going to register
    reg_name = input("What is the name of the user? ")

    #created a boolean and initialised it to true
    correct = True
    #used a for loop to read the textfile and split it
    for line in textfile:
        line1 = line.split(", ")
        
    #created a while loop
    while correct:

        #if the name is already in the textfile then it should print a statement and with the boolean it will return it to the main menu
        #used a break function so it doesnt loop infintely
        if reg_name == line1[0]:
            print("The name you have entered already exists in our database.")
            correct = True
            break

        #used an elif statement for a different condition
        #if the passwords do not match then the user can enter it again
        #set the boolean to false
        elif reg_name != line1[0]:
            reg_password = input("Please enter a password. ")
            confirm_reg_password = input(f"Please confirm your password.")
            correct = False

            # if the passwords do not match then the following will be executed
            #new inputs are placed 
            if reg_password != confirm_reg_password:
                print()
                print("Your name and password do not match please try again.")
                reg_name = input("What is the name of the user? ")
                reg_password = input("Please enter a password. ")
                confirm_reg_password = input(f"Please confirm {reg_name} password.")

                #once the passwords match then a print statement states it has been added to the textfiles
                #then a textfile will be opened and by using the writelines function it is able to write all the information to the textfile
                if reg_password == confirm_reg_password:
                    print(f"\nThank you {reg_name} has been added to our database. ")
                    textfile = open("user.txt","a")
                    textfile.writelines(f"\n{reg_name}, {confirm_reg_password}")
            
            #once the passwords match then a print statement states it has been added to the textfiles
            #then a textfile will be opened and by using the writelines function it is able to write all the information to the textfile
            elif reg_password == confirm_reg_password:
                print(f"\nThank you {reg_name} has been added to our database. ")
                textfile = open("user.txt","a")
                textfile.writelines(f"\n{reg_name}, {confirm_reg_password}")
                
#created a add task function
def add_task():

    #i imported the date and time
    import datetime
    from datetime import date

    #asked the user a series of questions that about the task and all of their inputs are stored and are wrote to the textfiles 
    add_name = input("To whom is the task being assigned to? ")
    task = input(f"What is the name of the task given to {add_name}? ")
    task_descrip = input("What is the description of the task? ")
    date_ass = date.today()
    due_date = input(f"When is the due date of the task? (YYYY-MM-DD) ")
    completion = input("Has the task been completed? (Yes or No) ").lower().capitalize()

    #opened the textfile
    text_file21 = open("tasks.txt","a")
    text_file21.writelines(f"\n{add_name}, {task}, {task_descrip}, {date_ass}, {due_date}, {completion}")
    print("Thank you the task has been added to the system.")
    #closed the textfile
    text_file21.close()

#created a view all function
def view_all():
    #opened a textfile
    #read a textfile and split it with a new line
    text_file2 = open("tasks.txt","r+")
    text_file3 = text_file2.read().split("\n")
    # x = 0
    #used a for loop that has a range from 0 to the len of the textfile
    #used indexing of and created a counter that will add 1 to each of them which makes it possible to view all the tasks
    for x in range(len(text_file3)):
        admin_task = text_file3[x].split(",")
        #used a print statement that will print all the tasks in a user friendly view
        print(f"Task\t\t: {admin_task[0]} \nAssigned to\t:{admin_task[1]}\nTask description:{admin_task[2]}\nDate assigned\t:{admin_task[3]}\nDue date\t:{admin_task[4]}\nTask Completion\t:{admin_task[5]}\n\n{spacer1}")
        x += 1
    #closed a textfile
    text_file2.close()
    
#created a view mine   
def view_mine():
    #opened a textfile
    #read all the lines
    view_task = open("tasks.txt","r")
    view_task2 = view_task.readlines()

    #created a variabe 
    count = "Task number: "

    #created a counter variable
    x = 1
    b = 0

    #used a for loop that has a range from 0 to the length of the textfile
    #used a condition if the name is equal the tasks textfile then it will print all the tasks that are assigned with the person that is logged in
    for b in range(len(view_task2)):
        task1 = view_task2[b].split(",")
        if name == task1[0]:
            name1 = (f"{count} {x}\nTask:\t{task1[1]} \nAssigned to :\t{task1[0]}\nTask description:\t{task1[2]}\nDate assigned:\t{task1[3]}\nDue date:\t{task1[4]}\nTask Complete?\t{task1[5]}\n{spacer1}")
            print(name1)
            #incremented the counting variable by adding 1 to it
            b += 1
            x += 1
    #closed the textfile
    view_task.close()

#created a view mine edit function
def view_mine_edit():

    #asked the user to input whether the task is completed or not
    cont = input("Would you like to edit your task? (Yes or No)\n").lower()
    print(spacer1)
    # repeat_admin = True
    #if the user enters yes then a print statement will ask the user which task they would like to edit
    if cont == "yes":
        task_edit_number = int(input("Please select a task number which you wish to edit  or  if you wish to return to main menu enter \"-1\".\n"))
        
        #if the user enters "-1" then the main menu will apear
        if task_edit_number == -1:
            repeat = False
        
        #used an else statement
        else:
            #created an empty list
            #opened a textfile and read it and split it and places all the information from the textfile into the list
            #with the number the user entered it was then possible to work with a specific task that the user has
            task_list = []
            text = open("tasks.txt","r")
            task_list = text.read().splitlines()
            task_list_item = task_list[task_edit_number-1].split(", ")
            print(spacer2)

            #printed a statement to show the user which task they selected
            print(f"You have selected task number {task_edit_number}")
            print(f"Please select one of the following options :")

            #used an input statement and made their answer lowercase using the .lower() function
            edit_task = input(f"\ne - edit the task\nm - mark the task as complete\n{spacer2}\n").lower()
            
            #if the input if equal to "m" 
            #by using the indexing i am able to make changes in the list 
            #usinf the join function i am able to join the tuple and after editing the list
            #i then made it equal to the task that the user selected and i minused 1 bcoz with coding a counter starts from 0 and not from 1
            if edit_task == "m":
                task_list_item[5] = "Yes"
                task_list_join = ", ".join(task_list_item)
                task_list[task_edit_number-1] = task_list_join

                #opened a textfile for a writing purpose
                task_file1 = open ("tasks.txt", "w")

                #using a for loop i am able to read the list i created (task_list)
                #by using the write function i am able to update the information to the textfile
                for item in task_list:
                    task_file1.write(f"{item}\n")
                #closed the textfile
                task_file1.close

                #printed a statement
                #set the boolean variable to false
                print(f"\nTask {task_edit_number} has been marked as complete.")
                repeat = False

            #an elif statement if "e" is is inputted
            #using an if statement to check if the index postion 5 is equal to "yes" then a print statement excecutes
            #set the boolean variable to False   
            elif edit_task == "e":
                if task_list_item[5] == "Yes":
                    print("You can only edit a incompleted task.")
                    repeat = False

                #else function
                else:
                    #asked the user to input what they want to edit and made their input into a lower case 
                    edit_choice = input(f"{spacer2}\nWhat would you like to edit from your task?\nPlease select one of the following:\n\nn - username\nd - due date\n{spacer2}\n").lower()

                    #if statement 
                    #using the join function i am able to join the tuple and after editing the list
                    #i then made it equal to the task that the user selected and i minused 1 bcoz with coding a counter starts from 0 and not from 1
                    if edit_choice == "n":
                        new_name = input("Enter the new username:\n")
                        task_list_item[0] = new_name
                        task_list_join = ", ".join(task_list_item)
                        task_list[task_edit_number-1] = task_list_join

                        #opened a textfile and read the list and wrote it to the textfile
                        new_name_textfile = open("tasks.txt", "w")
                        for name in task_list:
                            new_name_textfile.write(f"{name}\n")
                            print(f"Task{task_edit_number-1} has now been assigned to {name}")
                        
                        #closed the textfile
                        new_name_textfile.close()

                    #elif statement 
                    #using the join function i am able to join the tuple and after editing the list
                    #i then made it equal to the task that the user selected and i minused 1 bcoz with coding a counter starts from 0 and not from 1
                    
                    elif edit_choice == "d":
                        new_date = input("Enter the new due date (example: 25 Oct 2019)\n")
                        task_list_item[4] = new_date
                        task_list_join = ", ".join(task_list_item)
                        task_list[task_edit_number-1] = task_list_join

                        new_date_textfile = open("tasks.txt", "w")
                        for date in task_list:
                            new_date_textfile.write(f"{date}\n")
                            print(f"Task{task_edit_number-1} dates have been changed to {date}")
                        new_date_textfile.close()
                        return name
    #elif statement if the user entered "no"
    #set the boolean variable to false
    elif cont == "no":
        repeat_admin = False
        
#created a report function
def reports():

    # When the user chooses to generate reports, two text files, called task_overview.txt and user_overview.txt , should be generated

    #Import packages
    import datetime
    from datetime import date

    # the reports function writes reports in 2 different text files. The users_overview file and the task overview file.
    read_task3 = open ('tasks.txt', 'r')
    task_count_list = read_task3.read().splitlines()
    read_task3.close()
    list_length = len(task_count_list)
    #print(f"Total tasks is {list_length}")

    #counters used to count rhe number of tasks done, incomplete and overdue
    countYes = 0
    countNo = 0
    overdue = 0
    today = date.today() # stores the current date

    # counting the number of tasks completed and tasks that are not yet completed  
    for line in task_count_list:
        if "Yes" in line:
            countYes +=1
        else:
            countNo +=1
    #print (f"completed tasks is {countYes} and uncompleted is {countNo}")

    # taking each portion of the due date in order to convert it to a datetime format so that we can compare it to the current date and determin if a task is overdue
    for item in task_count_list:
        due_date = item.split(", ")[4]
        date_month = due_date[5:7]
        date_year = due_date[0:4]
        date_day = due_date[8::]

        # casting the due date into a date format
        dueDateInt = date(int(date_year), int(date_month), int(date_day))
        

        # comparing the dates to determine if the task is overdue
        if dueDateInt < today and "No" in item:
            overdue +=1
    #print(f"Overdue is {overdue}")
    # the following lines calculates the percentage of incomplete tasks and the percentage of tasks that are overdue.
    percentage_incomplete = (countNo/list_length) * 100
    #print(f"The percentage of incomplete tasks is {percentage_incomplete:.2f}%")
    percentage_overdue = (overdue/list_length) * 100
    #print(f"The percentage of overdue tasks is {percentage_overdue:.2f}%")

    # once all the necessary calculations are done, we write the results in the overview text file
    outfile = open('task_overview.txt', 'w')
    outfile.write(f"The total number of tasks is {list_length} \nThe total number of completed tasks are {countYes} \nThe total number of uncompleted tasks are {countNo} \nThe total number of tasks that are overdue and uncompleted are {overdue} \nThe percentage of incomplete tasks are {percentage_incomplete:.2f}% \nThe percentage of tasks that are overdue are {percentage_overdue:.2f}%")
    outfile.close()

    
    # the same logic used above is applied here but this time for each user. 
    open_overview = open ('user_overview.txt', 'w')
    line_out = ""

    #opened the textfile and read it and split its lines
    users_read = open ('user.txt', 'r')
    list_users = users_read.read().splitlines()
    #closed the textfile
    users_read.close()


    #found the length of the list using thelength function
    list_users_length = len(list_users)
    tasks_read = open ('tasks.txt', 'r')
    tasks_list = tasks_read.read().splitlines()
    tasks_list_length = len(tasks_list)
    #closed the textfile
    tasks_read.close()

    #for the following i created my counting variables and initilaised them to 0
    user_tasks_count = 0
    user_completed_tasksCount = 0
    user_incomplete_tasksCount = 0
    user_overdue_taskCount = 0




    usernames = [] # stores the usernames so that we can display details for each username
    user_tasks = []
    
    # for each username, we display the number of tasks assigned to that user, the percentage of tasks assigned to that user, the percentage of tasks completed, uncompleted and overdue.
    for line in list_users:
        usernames.append(line.split(", ")[0])

    # writing in the first line, the total number of users and tasks.
    # then for each user, we find the total number of tasks, the percentage of tasks completed, uncompleted and overdue.
    # To do this, we use counters which are set to 0 above and incremented once a specific condition is met.
    open_overview.write(f"The total number of users is {list_users_length} and the total number of tasks is {tasks_list_length}\n")
    for username in usernames:

        #used a for loop that reads the textfile and works from a range from 0 to the length of the textfile 
        #with indexung i was able to select a specific part of the textfile and convert it to an integer
        for task in range(0, len(tasks_list)):
            due_date1 = tasks_list[task].split(", ")[4]
            date_month1 = due_date1[5:7]
            date_year1 = due_date1 [0:4]
            date_day1 = due_date1 [8::]
            due_date_int1 = date(int(date_year1), int(date_month1), int(date_day1))
            today1 = date.today()

            #used an if statement , and 'in' and 'and' functions that were used to check if certain criteria are met anf if so the counting variable will increment by 1
            if f"{username}" in f"{tasks_list[task]}":
                user_tasks_count += 1


            if f"{username}" in f"{tasks_list[task]}" and "Yes" in f"{tasks_list[task]}":
                user_completed_tasksCount += 1


            if f"{username}" in f"{tasks_list[task]}" and "No" in f"{tasks_list[task]}":
                user_incomplete_tasksCount += 1


            if f"{username}" in f"{tasks_list[task]}" and "No" in f"{tasks_list[task]}" and due_date_int1 < today1:
                user_overdue_taskCount += 1

        #for the following below i then used the append function to update the list with the new information 
        # i then multiplied by 100       
        user_tasks.append(username)
        user_tasks.append(user_tasks_count)
        user_taskPer = round((user_tasks_count/tasks_list_length)*100, 2)

        user_tasks.append(user_completed_tasksCount)
        user_completed_tasksPer = round((user_completed_tasksCount/tasks_list_length)*100, 2)

        user_tasks.append(user_incomplete_tasksCount)
        user_incomplete_tasksPer = round((user_incomplete_tasksCount/tasks_list_length)*100, 2)

        user_tasks.append(user_overdue_taskCount)
        user_overdue_tasksPer = round((user_overdue_taskCount/tasks_list_length)*100, 2)

        # for each user, we write the necessary details in the user overview text file
        line_out = username + " " + "has" + " " + str(user_tasks_count) + " tasks, " + str(user_taskPer) + "%" + " of tasks, " + " " + str(user_completed_tasksPer) + "%" + " tasks completed" + ", " + str(user_incomplete_tasksPer) + "%" + " incomplete tasks" + ", "+ str(user_overdue_tasksPer) + "% " + " tasks overdue" + "\n"
        open_overview.write(line_out)
        # reseting the counters so that the calculations are done properly for each user.
        user_tasks_count = 0
        user_completed_tasksCount = 0
        user_incomplete_tasksCount = 0
        user_overdue_taskCount = 0

    #closed the textfile
    open_overview.close()


def display_statistics():

    choice = input (f"{spacer1}\nPlease select one of the following:\nu - users overview\nt - tasks_overview\n{spacer1}\n")
    # when admin chooses 'users overview', we create a list to store all the lines in the file users_overview.txt.
    # then the reports read from the text file is printed to the user in a user friendly manner.
    if choice.lower() == "u":
        user_overview = open ('user_overview.txt', 'r')
        user_overview_list = user_overview.read().splitlines()
        user_overview.close()
        for line1 in user_overview_list:
            print(line1)      

    # similarly, when the user chooses tasks overview, we create a list containing all the necessary details from the text file and we print the details in a user friendly manner.      
    elif choice.lower() == "t":
        task_overview = open('task_overview.txt', 'r')
        task_overview_list = task_overview.read().splitlines()
        task_overview.close()
        for line in task_overview_list:
            print(line)




text_file = open("user.txt","r+")
#variables that will print objects for a user friendly matter.
spacer = ("=" * 50)
spacer1 = ("-" * 50)
spacer2 = ("*" * 50)

#initialised my boolean variables to true in the beginning of the program
login_success = True
repeat = True
#asked the user to input their name and password
name = input("What is your username?").lower()
password = input("What is your password?").lower()

#created a while loop and initialised it to True
while login_success:
    #used a for loop that will read each line in the textfile    
    for line in text_file:
        #i then split the name and password with a comma in the textfile
        valid_user = line.split(", ")
        #created a new variable that stores the first index
        other_name = valid_user[0]
        #created a new variable that stores the second index and replaces a new line with a space
        other_password = valid_user[1].replace("\n","")
        #created an if statement if the variables are equal to the text to the textfile then the boolean is set to false and i stopped the loop with a break function
        if name == other_name and password == other_password:
            login_success = False
            break
#created another if statement with a condition if its not equal to the textfile then it loops through by asking the user to input their name and password again 
#i then closed the textfile and re-opened the textfile
#and set the boolean variable to true
    if name != other_name and password != other_password:
        print("Your login process is incorrect please try again! ")
        name = input("What is your username?")
        password = input("What is your password?")
        text_file.close()
        text_file = open("user.txt","r+")
        login_success = True

#created a new boolean variable and initialised it to true
repeat_admin = True
#created a counting variable and made it equal to 0
i = 0  
#created a while loop and made it equal to True
while True:
    

    #using an if statement that has conditions
    if name == "admin" and password == "adm1n":
        print(spacer1)#a variable that is used to make the program user friendly
        

        #asked the user to select the following using an input
        options = input(f"\nPlease select one of the following options:\nr  - Register user \na  - Add task \nva - View all tasks \nvm - View my tasks \ngr - Generate statistics \nds - Display Statistics \ne  - Exit \n {spacer}\n").lower()

        #used if statments and for certain options i placed a specific user defnined function
        #if a user selects one of these options a set function will run
        if options == "ds":
            display_statistics()

        if options == "r":
            reg_user()

        if options == "a":
            add_task()
                
        if options == "va":
            view_all()
            
        if options == "vm":
            view_mine()
            view_mine_edit()
            
        if options == "gr":
            print("Your reports have been generated into two textfiles 'task_overview' and 'user_overview'")
            reports()

        #for this condition a break function is being used to terminate the loop which exits the program
        if options == "e":
            break

            #login_success = False
        #break

    #used an elif statement if the passwords match as a security caution
    elif name == other_name and password == other_password:
        if repeat:
            print(spacer)
        #printed the other menu for the users
        options2 = input(f"\nPlease select one of the following options:\na  - add task \nva - view all tasks \nvm - view my tasks \ne  - exit \n {spacer}\n").lower()

        #an if statement if a user enters "a" a print statement will be executed
        if options2 == "a":
            print(spacer1)
            print("Sorry only admin is able to add tasks. ")
            print(spacer1)
            
            #a input statement if the user wnats to continue or exit
            options2_dash1 = input("Please select one of the following options :\nc - continue\ne - exit\n").lower()
            print(spacer)
            if options2_dash1 == "e":
                #breaks the loop
                break
            if options2_dash1 == "c":
                repeat = False
                text_file.close()
            
        #if the user selects any of these options the following user defined functions will be executed        
        if options2 == "va":
            view_all()
                 
        if options2 == "vm":
            view_mine()
            
        #for this condition a break function is being used to terminate the loop which exits the program
        if options2 == "e":
            break

#The end :)