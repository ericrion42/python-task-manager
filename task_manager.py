tasks = []

def add_task(title):
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    print(f"Task '{title}' added!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else: 
        for index, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{index + 1}. [{status}] {task['title']}")

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

