tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "2":
        for t in tasks:
            print("-", t)
    elif choice == "3":
        break