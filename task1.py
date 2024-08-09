def Disp_menu():
    print("To-Do List Menu: ")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def View(TODO):
    if not TODO:
        print("To-Do List is Empty!")
    else:
        print("Your To-Do List: ")
        for index, task in enumerate(TODO, start=1):
            print(f"{index}. {task}")

def AddTask(TODO):
    new_task=input("Enter Task: ")
    TODO.append(new_task)
    print("To-Do List updated Successfully!")

def RemoveTask(TODO):
    if TODO:
        try:
            task=int(input("Enter the index of the task you want to remove: "))-1
            if 0<=task<len(TODO):
                RemovedTask = TODO.pop(task)
                print(f"Task '{RemovedTask}' removed from To-Do List!")
            else:
                print("Invalid Index")
        except ValueError:
            print("Please Enter a Valid Number.")
            
def MarkCompleted(TODO):
    View(TODO)
    if TODO:
        try:
            task=int(input("Enter the index of the task to mark as completed: ")) - 1
            if 0 <= task < len(TODO):
                TODO[task] += " (Completed)"
                print("Task marked as completed.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please enter a valid integer index.")
    else:
        print("Your to-do list is empty.")
def main():
    TODO = []
    
    while True:
        Disp_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            View(TODO)
        elif choice == "2":
            AddTask(TODO)
        elif choice == "3":
            RemoveTask(TODO)
        elif choice == "4":
            MarkCompleted(TODO)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")



if __name__ == "__main__":
    main()
