import os

TASK_FILE = "tasks.txt"

def load_file():
    tasks = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE,'r',encoding="utf-8") as f:
            for line in f:
                text, status = line.strip().rsplit("||",1)#splits from the right side and atmost once hence the list only consists 2 elements
                tasks.append({"text": text, "done": status == "done"})
    return tasks

def save_task(tasks):
    with open(TASK_FILE,'w',encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']}||{status}\n")

def display_tasks(tasks):
    if not tasks:
        print("NO Tasks!")
    else:
        for i, task in enumerate(tasks,1):
            checkbox = "✅" if task["done"] else "❕"
            print(f"{i}. {checkbox} [{task['text']}]\n")
    print()

def task_manager():
    tasks = load_file()

    while True:
        print("\n------- TASK LIST MANAGER -------\n")
        print("1.Add task")
        print("2.View Tasks")
        print("3.Mark Task as complete")
        print("4.Delete Task")
        print("5.Exit")

        choice = int(input("Choose an option: "))
        match choice:
            case 1 : 
                task = input("enter your task: ").strip()
                if task:
                    tasks.append({"text":task, "done": False})
                    save_task(tasks)
                else:
                    print("Task cannot be empty!")     
            case 2:
                display_tasks(tasks)      
            case 3:
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number : "))
                    if 1 <= num <= len(tasks):
                        tasks[num-1]["done"] = True
                        save_task(tasks)
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("please enter a number.")
            case 4:
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num-1)
                        save_task(tasks)
                        print(f"Task removed {removed['text']}")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("please enter a number.")
            case 5:
                print("exiting task manager.....")
                break
            case _ :
                print("please choose a valid option")

task_manager()
            