import check_input
import tasklist
import task

# Name: Phu Nguyen, Sean Nightingale
# Date: 9/26/2023
# Desc: A program to help organize the user's tasks.

def main_menu():
    '''Displays the main menu and returns the user's input'''
    print("1. Display current task"+"\n"+"2. Display all tasks"+
          "\n"+"3. Mark current task complete"+"\n"+"4. Add new task"+
          "\n"+"5. Save and quit")
    menu_selection = check_input.get_int_range("Enter choice: ", 1, 5)
    return menu_selection


def get_date():
    '''Returns the properly formatted date of the newly added task'''
    month = check_input.get_int_range("Enter due date: \nEnter month: ", 1, 12)
    day = check_input.get_int_range("Enter day: ", 1, 31)
    year = check_input.get_int_range("Enter year: ", 2000, 3000)
    if int(day) < 10:
        day = f"0{day}"
    if int(month) < 10:
        month = f"0{month}"
    return f"{month}/{day}/{year}"


def get_time():
    '''Returns the properly formatted time of the newly added task'''
    hour = check_input.get_int_range("Enter time: \nEnter hour: ", 1, 24)
    minute = check_input.get_int_range("Enter minute: ", 0, 59)
    if int(hour) < 10:
        hour = f"0{hour}"
    if int(minute) < 10:
        hour = f"0{minute}"
    return f"{hour}:{minute}\n" #newline is for displaying task later on


def main():
    '''Calls functions to do what is asked by the user'''
    # test = task.Task("Book Flight to New York", "01/10/2024", "23:59")
    # print(test.description)
    list_of_task = tasklist.Tasklist()
    #print(tasklist.Tasklist())
    while True:
        num_task = len(list_of_task)
        print("-Tasklist-"+"\n"+f"Tasks to complete: {num_task}")
        choice = main_menu()
        if choice == 1:
            current_task = list_of_task[0]
            print(f"Current task is:\n{current_task}")
        elif choice ==2:
            print("Tasks: ")
            if not list_of_task:
                print("Good work! All tasks conpleted.")
            else:
                for tasks in list_of_task:
                    print(tasks, end="")
                print() #newline
        elif choice == 3:
            if list_of_task:
                print(f"Marking current task as complete:\n{list_of_task[0]}", end="")              
                list_of_task.mark_complete()
                print("New current task is:")
            if list_of_task:
                print(list_of_task[0])
            else:
                print("There are no tasks left.\n")
        elif choice == 4:
            desc = input("Enter a task: ")
            date = get_date()
            time = get_time()
            print() #newline
            list_of_task.add_task(desc, date, time)
        else:
            list_of_task.save_file()
            break


main()