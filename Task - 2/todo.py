tasks = []

def add_task(tasks):
    task = input("Enter new task : ")
    tasks.append(task)
    print(f"Task {task} added successfully!\n")

def view_tasks(tasks) :
    if not tasks :
        print("No tasks available.\n")
        return
    print("\nYour Tasks :")
    for index, task in enumerate(tasks, start = 1):
        print(f"{index}.{task}")
    print()

def remove_task(tasks) :
    if not tasks :
        print("No tasks available.\n")
        return
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to remove : "))
        print(f"Task '{tasks.pop(choice - 1)}' removed successfully!\n") if 1 <= choice <= len(tasks) else print("Invalid task number.\n")
    except ValueError :
        print("Please enter a valid number.\n")

def save_tasks(tasks):
    with open("TasksFile", "w") as file :
        for task in tasks:
            file.write(task + "\n")

if __name__ == "__main__" :
    print("---------------To-Do List---------------")
    while True :
        try :
            choice = int(input("1.Add Task   2.View Tasks   3.Remove Task   4.Exit\nChoice : "))
            while choice > 4 :
                choice = int(input("Choose a correct option(1,2,3,4) : "))
            if choice == 1 :
                add_task(tasks)
            elif choice == 2 :
                view_tasks(tasks)
            elif choice == 3 :
                remove_task(tasks)
            elif choice == 4 :
                break
            else:
                print("Invalid choice. Try again.\n")
        except :
            print("Value Error : Enter Numerical Value.\n")
        finally :
            save_tasks(tasks)