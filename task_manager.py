tasks = []

def add_task(title):
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    print(f"Task '{title}' added!")

add_task("Buy groceries")
print(tasks)  