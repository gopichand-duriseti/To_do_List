import os

FILE = "tasks.csv"

def load_tasks():
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            f.write("TASKS\n")
        return []

    with open(FILE, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines[1:]]  

def save_tasks(tasks):
    unique_tasks = list(dict.fromkeys(tasks))   
    with open(FILE, "w") as f:
        f.write("TASKS\n")
        for t in unique_tasks:
            f.write(t + "\n")


def add(task):
    task = task.strip()
    if task == "":
        return "Empty task not allowed."
    
    if task in tasks:
        return "Task already exists!"
    
    tasks.append(task)
    save_tasks(tasks)
    return f"'{task}' added successfully!"



def remove(task):
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        return f"'{task}' removed!"
    return f"'{task}' not found!"

def view():
    if not tasks:
        return "No tasks found."
    return "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks))

def modify(task):
    if task not in tasks:
        print(f"'{task}' not found!")
        return
    new = input("Enter new task name:\n")
    tasks[tasks.index(task)] = new
    save_tasks(tasks)
    print(f"Updated: '{task}' → '{new}'")


#MAIN CODE
tasks = load_tasks()

while True:
    print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Modify Task\n5. Exit")
    try:
        choice = int(input("Choice: "))
    except:
        print("Enter a number!")
        continue

    if choice == 1:
        print(add(input("Task:\n")))
    elif choice == 2:
        print(remove(input("Task to remove:\n")))
    elif choice == 3:
        print("\nYour Tasks:\n" + view())
    elif choice == 4:
        modify(input("Task to modify:\n"))
    elif choice == 5:
        print("Bye!")
        break
