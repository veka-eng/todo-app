def add_task(tasks, task):
    tasks.append(task)
    return tasks

if __name__ == "__main__":
    todo = []
    todo = add_task(todo, "Ma première tâche")
    print(todo)
