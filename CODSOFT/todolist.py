lists = {}

def create(name):
    lists[name] = []
    print(f"To-do list {name} created.")

def add(name, task):
    if name not in lists:
        create(name)
    lists[name].append(task)
    print(f"Task {task} added to list {name}.")

def remove(name, task):
    if name not in lists:
        print(f"List {name} does not exist.")
        return
    lists[name].remove(task)
    print(f"Task {task} removed from list {name}.")

def complete(name, task):
    if name not in lists:
        print(f"List {name} does not exist.")
        return
    for i in range(len(lists[name])):
        if lists[name][i] == task:
            lists[name][i] = "Completed"
            print(f"Task {task} marked as completed in list {name}.")
            break
    else:
        print(f"Task {task} not found in list {name}.")

def display(name):
    if name not in lists:
        print(f"List {name} does not exist.")
        return
    print(f"To-do list {name}:")
    for task in lists[name]:
        print(f"- {task}")

def save():
    with open("lists.txt", "w") as f:
        for list_name, list_tasks in lists.items():
            f.write(f"{list_name}: {', '.join(list_tasks)}\n")
    print("To-do lists saved.")

def loads():
    with open("lists.txt", "r") as f:
        for line in f:
            list_name, list_tasks = line.strip().split(":")
            lists[list_name] = list_tasks.split(",")
    print("To-do lists loaded.")

while True:
    print("\n1. Create List\n2. Add Task\n3. Remove Task\n4. Complete Task\n5. Display List\n6. Save Lists\n7. Load Lists\n8. Exit")
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        list_name = input("Enter the name of the list: ")
        create(list_name)

    elif choice == '2':
        list_name = input("Enter the name of the list: ")
        task = input("Enter the task to add: ")
        add(list_name, task)
    
    elif choice == '3':
        list_name = input("Enter the name of the list: ")
        task = input("Enter the task to remove: ")
        remove(list_name, task)

    elif choice == '4':
        list_name = input("Enter the name of the list: ")
        task = input("Enter the task to mark as completed: ")
        complete(list_name, task)

    elif choice == '5':
        list_name = input("Enter the name of the list: ")
        display(list_name)

    elif choice == '6':
        save()

    elif choice == '7':
        loads()

    elif choice == '8':
        print("Exiting the program")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
