RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

tasks = []

def add_task(title):
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    print(f"Task '{title}' added!")


def view_tasks(pause=False):
    if len(tasks) == 0:
        print("No tasks yet.")
    else: 
        for index, task in enumerate(tasks):
            status = f"{GREEN}✓{RESET}" if task["done"] else f"{RED}✗{RESET}"
            print(f"{index + 1}. [{status}] {task['title']}")
    if pause: 
        input("\nPress Enter to continue...")

def complete_task(index):
    if index < 0 or index >= len(tasks):
        print("Invalid task number!")
    else: 
        tasks[index]["done"] = True
        print(f"Task '{tasks[index]['title']}' marked as done!")

def delete_task(index):
    if index < 0 or index >= len(tasks):
        print("Invalid task number!")
    else: 
        removed = tasks.pop(index)
        print(f"Task '{removed['title']}' deleted!")

def main():
    while True:
        print("\n--- Task Manager ---")
        print(f"{YELLOW}1.{RESET} View tasks")
        print(f"{YELLOW}2.{RESET} Add task")
        print(f"{YELLOW}3.{RESET} Complete task")
        print(f"{YELLOW}4.{RESET} Delete task")
        print(f"{YELLOW}5.{RESET} Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_tasks(pause=True)
        elif choice == "2":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "3":
            view_tasks()
            task_num = int(input("Enter task number to complete: "))
            complete_task(task_num - 1)
        elif choice == "4":
            view_tasks()
            task_num = int(input("Enter task number to delete: "))
            delete_task(task_num - 1)
        elif choice == "5":
            print(f"{YELLOW}Goodbye!{RESET}")
            break
        else:
            print("Invalid choice, please try again!")

main()