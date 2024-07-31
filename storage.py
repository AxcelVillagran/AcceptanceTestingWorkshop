import os
from task import Task

class Storage:
    FILE_PATH = "tasks.txt"

    @staticmethod
    def save_tasks(tasks):
        with open(Storage.FILE_PATH, 'w') as file:
            for task in tasks:
                file.write(f"{task.id},{task.title},{task.description},{task.completed}\n")

    @staticmethod
    def load_tasks():
        tasks = []
        if os.path.exists(Storage.FILE_PATH):
            with open(Storage.FILE_PATH, 'r') as file:
                for line in file:
                    task_id, title, description, completed = line.strip().split(',')
                    task = Task(int(task_id), title, description)
                    task.completed = completed == "True"
                    tasks.append(task)
        return tasks
